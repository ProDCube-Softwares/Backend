import motor.motor_asyncio
from beanie import init_beanie

from Models import ContactUsModel, InternalUserModel


class Connection:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def connect(self) -> None:
        client = motor.motor_asyncio.AsyncIOMotorClient(self.host, self.port)
        await init_beanie(database=client.ProDCube, document_models=[ContactUsModel, InternalUserModel])
