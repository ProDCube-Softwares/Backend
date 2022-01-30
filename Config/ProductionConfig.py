from Config.AppSettings import AppSettings


class ProductionSettings(AppSettings):
    class Config:
        env_file = "production.env"
