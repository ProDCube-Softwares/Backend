from typing import List

from beanie.exceptions import DocumentNotFound

from Database import internalUserDb
from Schemas import ITULoginRequestSchema
from Utils import JWT, logger


class OpenApiController:
    @staticmethod
    async def internalLogin(loginData: ITULoginRequestSchema) -> List[bool | str]:
        logger.info(message="Inside OpenApi Controller", fileName=__name__, functionName="OpenApiController")
        try:
            user = await internalUserDb(email=loginData.email)
            if user is not None and user.verifyPassword(loginData.password):
                logger.info(message="Login successful", fileName="App.py", functionName="InternalLogin")
                payload = {"name": user.name, "email": user.email, "role": user.role}
                token = JWT.encodeToken(payload=payload)
                return [True, token]
            else:
                logger.info(message="Login failed", fileName="App.py", functionName="InternalLogin")
                return [False, ""]
        except DocumentNotFound as documentNotFound:
            logger.error(message=documentNotFound, functionName="OpenAPI Controller", fileName=__name__)
