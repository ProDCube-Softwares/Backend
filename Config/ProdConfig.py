from Config.AppConfig import AppConfig


class ProdConfig(AppConfig):
    class Config:
        env_file = "production.env"
