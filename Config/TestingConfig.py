from Config.AppConfig import AppConfig
from Constants import EnvTypes


class TestConfig(AppConfig):
    ENV: EnvTypes = EnvTypes.TEST

    class Config:
        env_file = "testing.env"
