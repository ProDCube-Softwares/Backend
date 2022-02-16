from fastapi.types import Callable

from Config import AppConfig
from Database.Connection import Connection


class Events:
    def __init__(self, settings: AppConfig):
        self.db = Connection(databaseName="ProDCube", host=settings.databaseUrl, port=int(settings.databasePort))

    def createStartAppHandler(self) -> Callable:
        async def startApp() -> None:
            self.db.connect()

        return startApp
