import logging
from typing import Any, Dict, List, Optional

from pydantic import BaseSettings

# from Config.BaseConfig import BaseAppSettings
from Constants import Constants, EnvTypes


class AppConfig(BaseSettings):
    debug: bool = False
    title: str = Constants.productionTitle
    version: str = Constants.version
    contact: Dict[str, str] = {"ProDCube": Constants.mail}
    allowedHosts: List[str] = ["*"]
    logging_level: int = logging.INFO
    description: str = Constants.productionDescription
    databaseUrl: str
    databasePort: Optional[str]
    secretKey: str
    ENV: EnvTypes = EnvTypes.PROD

    class Config:
        env_file = "production.env"
        validate_assignment = True

    @property
    def fastapiKwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "title": self.title,
            "version": self.version,
            "contact": self.contact,
        }
