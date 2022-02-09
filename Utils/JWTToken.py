from datetime import datetime, timedelta

from jose import JWTError, jwt

from Utils.Logger import logger

from .Environment import envSettings


class JWTToken:
    def __init__(self, secret: str):
        self.secret = secret

    def encodeToken(self, payload: dict) -> str:
        logger.info(message="Encoding JWT Token...", fileName=__name__, functionName="EncodeToken")
        expiry = datetime.utcnow() + timedelta(minutes=2)
        payloadCopy = payload.copy()
        payloadCopy.update({"exp": expiry})
        generatedToken = jwt.encode(payloadCopy, self.secret, algorithm="HS256")
        return generatedToken

    def decodeToken(self, token: str):
        logger.info(message="Decoding JWT Token...", fileName=__name__, functionName="DecodeToken")
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload
        except JWTError as jwtError:
            logger.error(message=str(jwtError), fileName=__name__, functionName="DecodeToken")
            return jwtError


JWT = JWTToken(secret=envSettings.secretKey)
