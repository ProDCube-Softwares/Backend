from beanie.exceptions import DocumentNotFound
from fastapi import APIRouter, Depends, Request
from starlette import status
from starlette.responses import RedirectResponse

from Controller import OpenApiController
from Schemas import ITULoginRequestSchema
from Utils import logger, templates

openApiDocRouter = APIRouter(tags=["OpenAPI Specifications"])


@openApiDocRouter.post("/internalLogin", name="Internal Login")
async def internalLogin(request: Request,
                        loginData: ITULoginRequestSchema = Depends(ITULoginRequestSchema.asForm)):
    logger.info(message="Entered Internal Login view", fileName=__name__, functionName="InternalLogin")
    try:
        res, token = await OpenApiController.internalLogin(loginData=loginData)
        if res:
            redirectResponse = RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)
            redirectResponse.set_cookie(key="token", value=token)
            return redirectResponse
        else:
            return templates.TemplateResponse("401.html", {"request": request})
    except DocumentNotFound as documentNotFoundException:
        logger.error(message=documentNotFoundException, fileName=__name__, functionName="InternalLogin")
