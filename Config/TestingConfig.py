from Config.AppSettings import AppSettings


class TestSettings(AppSettings):
    class Config:
        env_file = "testing.env"
