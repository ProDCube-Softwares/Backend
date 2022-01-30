import logging

from Config.AppConfig import AppConfig
from Constants import Constants, EnvTypes


class DevelopmentConfig(AppConfig):
    debug = True
    title = Constants.developmentTitle
    description = Constants.developmentDescription
    ENV: EnvTypes = EnvTypes.DEV

    loggingLevel: int = logging.DEBUG

    class Config:
        env_file = "development.env"
