import logging

from Config.AppSettings import AppSettings
from Constants import Constants, EnvTypes


class DevelopmentSettings(AppSettings):
    debug = True
    title = Constants.developmentTitle
    description = Constants.developmentDescription
    ENV: EnvTypes = EnvTypes.DEV

    loggingLevel: int = logging.DEBUG

    class Config:
        env_file = "development.env"
