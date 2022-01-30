from functools import lru_cache
from typing import Type, Dict

from Config.AppConfig import AppConfig
from Config.DevelopmentConfig import DevelopmentConfig
from Config.ProductionConfig import ProductionConfig
from Constants import EnvTypes
from Utils.Environment import Environment

environments: Dict[EnvTypes, Type[AppConfig]] = {
    EnvTypes.PROD: ProductionConfig,
    EnvTypes.DEV: DevelopmentConfig,
}


@lru_cache()
def generateSettings() -> AppConfig:
    currentEnv = Environment.getSettingsByEnvironment()
    config = environments[currentEnv]
    return config()
