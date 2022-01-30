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
