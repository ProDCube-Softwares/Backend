import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from httpx import AsyncClient, HTTPStatusError
from jinja2 import Environment, FileSystemLoader
from mongoengine import SaveConditionError

from Database import ContactUsDb
from Schemas import ContactUsRequestSchema
from Utils import envSettings, logger


class ContactUsController:

    def __init__(self):
        self.server = smtplib.SMTP("smtp.gmail.com", 25)

        self.server.starttls()

        self.server.login(envSettings.email, envSettings.emailPassword)

        self.customerMail = MIMEMultipart()
        self.ourMail = MIMEMultipart()

        self.fileLoader = FileSystemLoader("Templates/Html")
        self.env = Environment(loader=self.fileLoader)

    @staticmethod
    async def getLocation():
        logger.info(message="Inside getLocation method of ContactUsController", fileName=__name__,
                    functionName="Get Location")
        try:
            url: str = f"https://ipinfo.io?token={envSettings.ipAccessKey.strip()}"
            client = AsyncClient()
            response = await client.get(url)
            data = response.json()
            return {"country": data["country"], "region": data["region"]}
        except HTTPStatusError as httpStatusError:
            logger.error(message=httpStatusError, functionName="Get Location", fileName=__name__)

    def sendMailToCustomer(self, contactUsData: ContactUsRequestSchema):
        logger.info(message="Inside Send Mail to Customer method of ContactUsController", fileName=__name__,
                    functionName="Send Mail to Customer")
        try:
            self.customerMail["From"] = "ProDCube"
            self.customerMail["Subject"] = "Thanks for Contacting ProDCube"
            template = self.env.get_template("email.html")
            htmlContent = template.render(name=contactUsData.name)
            self.customerMail.attach(
                MIMEText(htmlContent, "html"))
            message = self.customerMail.as_string()
            self.server.sendmail(envSettings.email, contactUsData.email, message)
        except smtplib.SMTPConnectError as smtpConnectError:
            logger.error(message=smtpConnectError, fileName=__name__, functionName="Send Mail to Customer")
        except smtplib.SMTPAuthenticationError as smtpAuthError:
            logger.error(message=smtpAuthError, fileName=__name__, functionName="Send Mail to Customer")

    def sendMailToUs(self, contactUsData: ContactUsRequestSchema):
        logger.info(message="Inside Send Mail to Us method of ContactUsController", fileName=__name__,
                    functionName="Send Mail to Us")
        try:
            self.ourMail["From"] = contactUsData.name
            self.ourMail["Subject"] = f"Message from {contactUsData.name} for ProDCube"
            self.ourMail.attach(
                MIMEText(contactUsData.message, "plain"))
            message = self.ourMail.as_string()
            self.server.sendmail(contactUsData.email, envSettings.email, message)
        except smtplib.SMTPConnectError as smtpConnectError:
            logger.error(message=smtpConnectError, fileName=__name__, functionName="Send Mail to Customer")
        except smtplib.SMTPAuthenticationError as smtpAuthError:
            logger.error(message=smtpAuthError, fileName=__name__, functionName="Send Mail to Customer")

    async def saveAndNotify(self, contactUsData: ContactUsRequestSchema):
        logger.info(message="Inside save method of ContactUsController", fileName=__name__, functionName="Save")
        try:
            await ContactUsDb.save(contactUsData)
            logger.info(message="ContactUs Data saved successfully", fileName=__name__, functionName="Save")
            self.sendMailToUs(contactUsData)
            self.sendMailToCustomer(contactUsData)
        except SaveConditionError as docAlreadyCreated:
            logger.error(message=docAlreadyCreated, fileName=__name__, functionName="Contact Us Controller")
