from fastapi import APIRouter
from httpx import AsyncClient
from mongoengine import SaveConditionError
from starlette.responses import JSONResponse

from Controller import ContactUsController
from Schemas import ContactUsRequestSchema
from Utils import logger

contactUsRouter = APIRouter(prefix="/contact-us", tags=["Contact Us"])
client = AsyncClient()


@contactUsRouter.post("", name="Contact Us")
async def contactUs(contactUsData: ContactUsRequestSchema):
    logger.info(message="Entered Contact Us Login view", fileName=__name__, functionName="Contact Us")
    try:
        response = await ContactUsController.getLocation()
        contactUsData.country = response["country"]
        contactUsData.region = response["region"]
        await ContactUsController().saveAndNotify(contactUsData)
        logger.info(message="Exited Contact Us Login view", fileName=__name__, functionName="Contact Us")
        return JSONResponse(status_code=200,
                            content={"status": "Success", "message": "Message has been sent successfully"})
    except SaveConditionError as saveConditionError:
        logger.error(message=saveConditionError, fileName=__name__, functionName="Contact Us")
