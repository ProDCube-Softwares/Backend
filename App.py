import asyncio
from pathlib import Path
from typing import List

from fastapi import FastAPI, Request, Depends
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from Config import generateSettings, AppConfig
from Config.Events import Events
from Database import Connection
from Utils import Utils, logger, templates
from Views import internalLogin
from Views import openApiDocRouter


def createFastApp() -> List[FastAPI | AppConfig]:
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
    return [app, appSettings]


fastApp, settings = createFastApp()


def getCookies(request: Request) -> str:
    cookies: str = request.cookies.get("token")
    if cookies is None:
        logger.error(message="No token found", functionName="Get Cookies", fileName="App.py")
        return ""
    return cookies


@fastApp.get("/docs", tags=["OpenAPI Specifications"])
async def getDocumentation(request: Request, token: str = Depends(getCookies)):
    if token is not None and len(token) != 0:
        logger.info(message="Getting documentation", functionName="Get Documentation", fileName="App.py")
        return get_swagger_ui_html(openapi_url="/openapi.json", title=settings.title)
    else:
        return templates.TemplateResponse("401.html", {"request": request})


@fastApp.get("/openapi.json", tags=["OpenAPI Specifications"])
async def getOpenApi(request: Request, token: str = Depends(getCookies)):
    if token is not None and len(token) != 0:
        logger.info(message="Getting OpenAPI", functionName="Get OpenAPI", fileName="App.py")
        return get_openapi(title=settings.title, version="1.0.0", routes=fastApp.routes)
    else:
        return templates.TemplateResponse("401.html", {"request": request})


@fastApp.get("/redoc", tags=["OpenAPI Specifications"])
async def getRedoc(request: Request, token: str = Depends(getCookies)):
    if token is not None and len(token) != 0:
        logger.info(message="Getting ReDoc", functionName="Get ReDoc", fileName="App.py")
        return get_redoc_html(openapi_url="/openapi.json", title=settings.title)
    else:
        return templates.TemplateResponse("401.html", {"request": request})


Utils.updateSchemaName(app=fastApp, function=internalLogin, name="Internal User Login Schema")
