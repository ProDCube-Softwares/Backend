from mongoengine import ConnectionFailure, connect

from Utils import logger


class Connection:
    def __init__(self, databaseName: str, host: str, port: int):
        self.host = host
        self.port = port
        self.databaseName = databaseName

    def connect(self) -> None:
        try:
            logger.info(message="Connecting to MongoDB....", fileName=__name__, functionName="Connect")
            connect(db=self.databaseName, host=self.host, port=self.port)
            logger.info(message="Connected to MongoDB", fileName=__name__, functionName="Connect")
        except ConnectionFailure as connectionFailure:
            logger.critical(message="Connection Error: " + connectionFailure.__str__(), fileName=__name__,
                            functionName="Connect")
