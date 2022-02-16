from typing import List

from mongoengine import DoesNotExist

from Database import internalUserDb
from Utils import JWT, logger


class OpenApiController:
    @staticmethod
    def internalLogin(email: str, password: str) -> List[bool | str] | None:
        logger.info(message="Inside OpenApi Controller", fileName=__name__, functionName="OpenApiController")
        try:
            user = internalUserDb(email=email)
            if user is not None and user.verifyPassword(password):
                logger.info(message="Login successful", fileName="App.py", functionName="InternalLogin")
                payload = {"name": user.name, "email": user.email, "role": user.role}
                token = JWT.encodeToken(payload=payload)
                return [True, token]
            else:
                logger.info(message="Login failed", fileName="App.py", functionName="InternalLogin")
                return [False, ""]
        except DoesNotExist as documentNotFound:
            logger.error(message=documentNotFound, functionName="OpenAPI Controller", fileName=__name__)
            return None
