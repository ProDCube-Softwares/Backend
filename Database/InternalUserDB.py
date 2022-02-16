from mongoengine import DoesNotExist

from Models import InternalUserModel
from Utils import logger


def internalUserDb(email: str) -> InternalUserModel | None:
    logger.info(message="Inside Internal User Db --- Fetching Data...", functionName="Internal User DB",
                fileName=__name__)
    try:
        user: InternalUserModel = InternalUserModel.objects.get(email=email)
        return user
    except DoesNotExist as documentNotFound:
        logger.error(message=documentNotFound, functionName="Internal User DB", fileName=__name__)
        return None
