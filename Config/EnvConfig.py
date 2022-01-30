from functools import lru_cache
from typing import Dict, Type

from Config.AppSettings import AppSettings
from Config.DevelopmentSettings import DevelopmentSettings
from Config.ProductionSettings import ProductionSettings
from Constants import EnvTypes

environments: Dict[EnvTypes, Type[AppSettings]] = {
    EnvTypes.PROD: ProductionSettings,
    EnvTypes.DEV: DevelopmentSettings,
}


@lru_cache()
def generateSettings() -> AppSettings:
    env = DevelopmentSettings().ENV
    config = environments[env]
    return config()
