from fastapi.types import Callable

from Config import AppConfig
from Database.Connection import Connection


class Events:
    def __init__(self, settings: AppConfig):
        self.db = Connection(settings.databaseUrl, int(settings.databasePort))

    def createStartAppHandler(self) -> Callable:
        async def startApp() -> None:
            await self.db.connect()

        return startApp
