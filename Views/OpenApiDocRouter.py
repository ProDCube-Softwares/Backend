from beanie.exceptions import DocumentNotFound
from fastapi import APIRouter, Request, Depends, Response

from Controller import openApiController
from Models import ITULoginRequestModel
from Utils import logger, templates

# from starlette import status
# from starlette.responses import RedirectResponse

openApiDocRouter = APIRouter(tags=["OpenAPI Specifications"])


@openApiDocRouter.post("/internalLogin", name="Internal Login")
async def internalLogin(request: Request, response: Response = Response(),
                        loginData: ITULoginRequestModel = Depends(ITULoginRequestModel.asForm)):
    logger.info(message="Entered Internal Login view", fileName="App.py", functionName="InternalLogin")
    try:
        res, token = await openApiController(loginData=loginData)
        if res:
            response.set_cookie(key="token", value=token)
            return {"message": "Login Successful"}
            # return RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)
        else:
            return templates.TemplateResponse("401.html", {"request": request})
    except DocumentNotFound as documentNotFoundException:
        logger.error(message=documentNotFoundException, fileName="App.py", functionName="InternalLogin")


@openApiDocRouter.get("/")
def home(request: Request):
    logger.info(message="Entered Home page view", fileName="App.py", functionName="Home")
    logger.info(message="Exited Home page view", fileName="App.py", functionName="Home")
    return templates.TemplateResponse("index.html", {"request": request})
