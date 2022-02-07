from beanie.exceptions import DocumentNotFound

from Models import InternalUserModel
from Utils import logger


async def internalUserDb(email: str) -> InternalUserModel:
    logger.info(message="Inside Internal User Db --- Fetching Data...", functionName="Internal User DB",
                fileName=__name__)
    try:
        user: InternalUserModel = await InternalUserModel.find_one(InternalUserModel.email == email)
        return user
    except DocumentNotFound as documentNotFound:
        logger.error(message=documentNotFound, functionName="Internal User DB", fileName=__name__)
