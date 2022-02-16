from fastapi import APIRouter, Request, Form
from mongoengine import DoesNotExist
from starlette import status
from starlette.responses import RedirectResponse

from Controller import OpenApiController
from Utils import logger, templates

openApiDocRouter = APIRouter(tags=["OpenAPI Specifications"])


@openApiDocRouter.post("/internalLogin", name="Internal Login")
async def internalLogin(request: Request,
                        email: str = Form(...),
                        password: str = Form(...)):
    logger.info(message="Entered Internal Login view", fileName=__name__, functionName="InternalLogin")
    try:
        res, token = OpenApiController.internalLogin(email=email, password=password)
        if res:
            redirectResponse = RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)
            redirectResponse.set_cookie(key="token", value=token)
            logger.info(message="Exited Internal Login view", fileName=__name__, functionName="InternalLogin")
            return redirectResponse
        else:
            logger.info(message="Exited Internal Login view", fileName=__name__, functionName="InternalLogin")
            return templates.TemplateResponse("401.html", {"request": request}, status_code=404)
    except DoesNotExist as documentNotFoundException:
        logger.error(message=documentNotFoundException, fileName=__name__, functionName="InternalLogin")
