from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

from Config.EnvConfig import generateSettings

load_dotenv()

router = APIRouter()


def createFastApp() -> FastAPI:
    appSettings = generateSettings()
    app = FastAPI(**appSettings.fastapi_kwargs, base_url="/api/v1")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=appSettings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


fastApp = createFastApp()
