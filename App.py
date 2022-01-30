from pathlib import Path

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from Config import generateSettings
from Config.Events import Events
from Utils import templates


def createFastApp() -> FastAPI:
    appSettings = generateSettings()
    events = Events(appSettings)

    app = FastAPI(**appSettings.fastapiKwargs)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=appSettings.allowedHosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_event_handler("startup", events.createStartAppHandler())
    app.mount("/static", StaticFiles(directory=Path(__file__).parent / "Static/"), name="static")
    return app


fastApp = createFastApp()


@fastApp.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
