from beanie.exceptions import DocumentNotFound
from fastapi import Response

from Database import internalUserDb
from Models import ITULoginRequestModel
from Utils import logger, JWT


async def openApiController(loginData: ITULoginRequestModel, response: Response) -> bool:
    logger.info(message="Inside OpenApi Controller", fileName=__name__, functionName="OpenApiController")
    try:
        user = await internalUserDb(email=loginData.email)
        if user is not None and user.verifyPassword(loginData.password):
            logger.info(message="Login successful", fileName="App.py", functionName="InternalLogin")
            payload = {"name": user.name, "email": user.email, "role": user.role}
            token = JWT.encodeToken(payload=payload)
            response.set_cookie(key="token", value=token)
            return True
        else:
            logger.info(message="Login failed", fileName="App.py", functionName="InternalLogin")
            return False
    except DocumentNotFound as documentNotFound:
        logger.error(message=documentNotFound, functionName="OpenAPI Controller", fileName=__name__)
