from typing import Dict, Type

from Config import AppConfig, DevelopmentConfig, ProductionConfig
from Constants import EnvTypes

environments: Dict[EnvTypes, Type[AppConfig]] = {
    EnvTypes.PROD: ProductionConfig,
    EnvTypes.DEV: DevelopmentConfig,
}
