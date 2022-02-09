from beanie.exceptions import DocumentAlreadyCreated
from httpx import AsyncClient

from Database import ContactUsDb
from Schemas import ContactUsRequestSchema
from Utils import logger


class ContactUsController:

    @staticmethod
    async def getLocation():
        logger.info(message="Inside getLocation method of ContactUsController", fileName=__name__,
                    functionName="Get Location")
        try:
            client = AsyncClient()
            response = await client.get("https://ipinfo.io?token=262ec427b3c2f7")
            data = response.json()
            return {"country": data["country"], "region": data["region"]}
        except Exception as exception:
            logger.error(message=exception, functionName="Get Location", fileName=__name__)

    @staticmethod
    async def saveAndNotify(contactUsData: ContactUsRequestSchema):
        logger.info(message="Inside save method of ContactUsController", fileName=__name__, functionName="Save")
        try:
            await ContactUsDb.save(contactUsData)
        except DocumentAlreadyCreated as docAlreadyCreated:
            logger.error(message=docAlreadyCreated, fileName=__name__, functionName="Contact Us Controller")
