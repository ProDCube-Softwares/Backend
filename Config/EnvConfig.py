from functools import lru_cache
from typing import Type, Dict

from Config.AppConfig import AppConfig
from Config.DevelopmentConfig import DevelopmentConfig
from Config.ProductionConfig import ProductionConfig
from Constants import EnvTypes
from Utils import logger
from Utils.Environment import Environment

environments: Dict[EnvTypes, Type[AppConfig]] = {
    EnvTypes.PROD: ProductionConfig,
    EnvTypes.DEV: DevelopmentConfig,
}


@lru_cache()
def generateSettings() -> AppConfig:
    functionDesc = "GenerateSettings"
    fileName = __name__.rsplit(".", maxsplit=1)[-1]
    currentEnv = Environment.getSettingsByEnvironment()
    if currentEnv.value == "dev":
        logger.info(fileName=fileName, functionName=functionDesc, message="Using Development Environment Config")
    elif currentEnv.value == "prod":
        logger.warning(fileName=fileName, functionName=functionDesc, message="Using Production Environment Config")
    elif currentEnv.value == "test":
        logger.warning(fileName=fileName, functionName=functionDesc, message="Using Testing Environment Config")
    config = environments[currentEnv]
    logger.info(fileName=fileName, functionName=functionDesc, message=f"Config Loaded exiting {functionDesc}")
    return config()
