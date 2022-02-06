from Config.DevelopmentConfig import DevelopmentConfig
from Config.ProductionConfig import ProductionConfig
from Config.TestingConfig import TestConfig
from Constants import EnvTypes


class Environment:
    @staticmethod
    def getSettingsByEnvironment() -> EnvTypes:
        with open("config.env", "r", encoding="utf-8") as configFile:
            config = configFile.readlines()[0].split("=")[1].strip("\"")
            if config == "production":
                return ProductionConfig().ENV
            elif config == "testing":
                return TestConfig().ENV
            elif config == "development":
                return DevelopmentConfig().ENV
            else:
                return DevelopmentConfig().ENV

    @staticmethod
    def getSecretKey() -> str:
        currentEnv = Environment.getSettingsByEnvironment()
        secretKey: str = ""
        if currentEnv.value == "dev":
            with open("development.env", "r", encoding="utf-8") as devEnv:
                secretKey = devEnv.readlines()[2].split("=")[1].strip("\"")
        elif currentEnv.value == "prod":
            with open("production.env", "r", encoding="utf-8") as prodEnv:
                secretKey = prodEnv.readlines()[2].split("=")[1].strip("\"")
        elif currentEnv.value == "test":
            with open("testing.env", "r", encoding="utf-8") as testEnv:
                secretKey = testEnv.readlines()[2].split("=")[1].strip("\"")
        return secretKey
