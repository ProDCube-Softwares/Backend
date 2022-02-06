from beanie.exceptions import DocumentNotFound
from fastapi import APIRouter, Request, Response, Depends

from Models import ITULoginRequestModel, InternalUserModel
from Utils import logger, templates, JWT

openApiDocRouter = APIRouter(tags=["OpenAPI Specifications"])


@openApiDocRouter.post("/internalLogin", name="Internal Login")
async def internalLogin(response: Response, loginData: ITULoginRequestModel = Depends(ITULoginRequestModel.asForm)):
    logger.info(message="Entered internalLogin view", fileName="App.py", functionName="InternalLogin")
    try:
        user: InternalUserModel = await InternalUserModel.find_one(InternalUserModel.email == loginData.email)
        if user.verifyPassword(loginData.password):
            logger.info(message="Login successful", fileName="App.py", functionName="InternalLogin")
            payload = {"name": user.name, "email": user.email, "role": user.role}
            token = JWT.encodeToken(payload=payload)
            response.set_cookie(key="token", value=token)
            return {"status": "Success", "message": "Login successful", "token": token}
        else:
            logger.info(message="Login failed", fileName="App.py", functionName="InternalLogin")
            return {"status": "Failure", "message": "Invalid password"}
    except DocumentNotFound as documentNotFoundException:
        logger.error(message=documentNotFoundException, fileName="App.py", functionName="InternalLogin")


@openApiDocRouter.get("/")
def home(request: Request):
    logger.info(message="Entered Home page view", fileName="App.py", functionName="Home")
    logger.info(message="Exited Home page view", fileName="App.py", functionName="Home")
    return templates.TemplateResponse("index.html", {"request": request})
