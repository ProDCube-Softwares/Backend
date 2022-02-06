import asyncio
from pathlib import Path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from Config import generateSettings, AppConfig
from Config.Events import Events
from Database import Connection
from Utils import Utils
from Views import internalLogin
from Views import openApiDocRouter


def createFastApp() -> FastAPI:
    appSettings: AppConfig = generateSettings()
    events = Events(appSettings)
    loop = asyncio.get_event_loop()
    dataBase = Connection(host=appSettings.databaseUrl, port=int(appSettings.databasePort))
    loop.create_task(dataBase.connect())
    app: FastAPI = FastAPI(**appSettings.fastapiKwargs)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=appSettings.allowedHosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_event_handler("startup", events.createStartAppHandler())
    app.mount("/static", StaticFiles(directory=Path(__file__).parent / "Static/"), name="static")
    app.include_router(openApiDocRouter)
    return app


fastApp = createFastApp()

Utils.updateSchemaName(app=fastApp, function=internalLogin, name="Internal User Login Schema")
