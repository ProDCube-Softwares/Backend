from beanie.exceptions import DocumentAlreadyCreated
from fastapi import APIRouter
from httpx import AsyncClient
from starlette.responses import JSONResponse

from Controller import ContactUsController
from Schemas import ContactUsRequestSchema
from Utils import logger

contactUsRouter = APIRouter(prefix="/contact-us", tags=["Contact Us"])
client = AsyncClient()


@contactUsRouter.post("", name="Contact Us")
async def contactUs(contactUsData: ContactUsRequestSchema):
    logger.info(message="Contact Us Login view", fileName=__name__, functionName="Contact Us")
    try:
        response = await ContactUsController.getLocation()
        contactUsData.country = response["country"]
        contactUsData.region = response["region"]
        await ContactUsController().saveAndNotify(contactUsData)
        return JSONResponse(status_code=200,
                            content={"status": "Success", "message": "Message has been sent successfully"})
    except DocumentAlreadyCreated as documentAlreadyCreated:
        logger.error(message=documentAlreadyCreated, fileName=__name__, functionName="Contact Us")
