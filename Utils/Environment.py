from Config import AppConfig
from Config.DevelopmentConfig import DevelopmentConfig
from Config.ProdConfig import ProdConfig
from Config.TestingConfig import TestConfig
from Constants import EnvTypes
from Constants.EnvironmentsDict import environments


class Environment:
    @staticmethod
    def getSettingsByEnvironment() -> EnvTypes:
        with open("config.env", "r", encoding="utf-8") as configFile:
            config = configFile.readlines()[0].split("=")[1].strip("\"").strip()
            if config == "production":
                return ProdConfig().ENV
            elif config == "testing":
                return TestConfig().ENV
            elif config == "development":
                return DevelopmentConfig().ENV
            else:
                return DevelopmentConfig().ENV

    def generateSettings(self) -> AppConfig:
        currentEnv = self.getSettingsByEnvironment()
        config = environments[currentEnv]
        return config()


envSettings: AppConfig = Environment().generateSettings()
