from beanie.exceptions import DocumentAlreadyCreated

from Models import ContactUsModel
from Schemas import ContactUsRequestSchema
from Utils import logger


class ContactUsDb:
    @staticmethod
    async def save(data: ContactUsRequestSchema):
        logger.info(message="Inside save method of ContactUsDb", fileName=__name__, functionName="Save")
        try:
            contactUsObj = ContactUsModel(**data.dict())
            contactUsObj.assignDate()
            await contactUsObj.insert()
        except DocumentAlreadyCreated as docAlreadyCreated:
            logger.error(message=docAlreadyCreated, fileName=__name__, functionName="Save")
