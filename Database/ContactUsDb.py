from mongoengine import SaveConditionError

from Models import ContactUsModel
from Schemas import ContactUsRequestSchema
from Utils import logger


class ContactUsDb:
    @staticmethod
    async def save(data: ContactUsRequestSchema):
        logger.info(message="Inside save method of ContactUsDb", fileName=__name__, functionName="Save")
        try:
            contactUsObj = ContactUsModel(**data.dict())
            contactUsObj.save()
        except SaveConditionError as saveConditionError:
            logger.error(message=saveConditionError, fileName=__name__, functionName="Save")
