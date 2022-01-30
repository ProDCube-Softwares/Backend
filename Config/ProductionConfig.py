from Config.AppConfig import AppConfig


class ProductionConfig(AppConfig):
    class Config:
        env_file = "production.env"
