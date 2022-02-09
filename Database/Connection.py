import motor.motor_asyncio
from beanie import init_beanie

from Models import ContactUsModel, InternalUserModel
from Utils import logger


class Connection:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def connect(self) -> None:
        try:
            logger.info(message="Connecting to MongoDB....", fileName=__name__, functionName="Connect")
            client = motor.motor_asyncio.AsyncIOMotorClient(self.host, self.port)
            logger.info(message="Connected to MongoDB", fileName=__name__, functionName="Connect")
            logger.info(message="Initializing models....", fileName=__name__, functionName="Connect")
            await init_beanie(database=client.ProDCube, document_models=[ContactUsModel, InternalUserModel])
            logger.info(message="Initialized models", fileName=__name__, functionName="Connect")
        except Exception as exception:
            logger.critical(message=exception, fileName=__name__, functionName="Connect")
