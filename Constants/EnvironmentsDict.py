from typing import Dict, Type

from Config import AppConfig, DevelopmentConfig
from Config.ProdConfig import ProdConfig
from Config.TestingConfig import TestConfig
from Constants import EnvTypes

environments: Dict[EnvTypes, Type[AppConfig]] = {
    EnvTypes.PROD: ProdConfig,
    EnvTypes.DEV: DevelopmentConfig,
    EnvTypes.TEST: TestConfig,
}
