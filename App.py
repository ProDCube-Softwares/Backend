import asyncio
from pathlib import Path
from typing import List

from fastapi import Depends, FastAPI, Request
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

from Config import AppConfig, generateSettings
from Config.Events import Events
from Database import Connection
from Utils import Utils, logger, templates
from Views import contactUs, contactUsRouter, internalLogin, openApiDocRouter


def createFastApp() -> List[FastAPI | AppConfig]:
    appSettings: AppConfig = generateSettings()
    dataBase = Connection(host=appSettings.databaseUrl, port=int(appSettings.databasePort))
    events = Events(appSettings)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
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
    app.include_router(contactUsRouter)
    return [app, appSettings]


fastApp, settings = createFastApp()


def getCookies(request: Request) -> str:
    logger.info(message="Getting Cookies", fileName="App.py", functionName="getCookies")
    cookies: str = request.cookies.get("token")
    if cookies is None:
        logger.error(message="No token found", functionName="Get Cookies", fileName="App.py")
        return ""
    return cookies


@fastApp.get("/", name="Home", tags=["Home"])
def home(request: Request):
    logger.info(message="Home page view", fileName="App.py", functionName="Home")
    token = getCookies(request=request)
    if token is not None and len(token) != 0:
        logger.info(message="Exited Home page view and Redirected", fileName="App.py", functionName="Home")
        return RedirectResponse("/docs")
    logger.info(message="Exited Home page view - UnAuthorized", fileName="App.py", functionName="Home")
    return templates.TemplateResponse("index.html", {"request": request})


@fastApp.get("/docs", name="Get Documentation", tags=["OpenAPI Specifications"])
async def getDocumentation(request: Request, token: str = Depends(getCookies)):
    if token is not None and len(token) != 0:
        logger.info(message="Getting documentation", functionName="Get Documentation", fileName="App.py")
        return get_swagger_ui_html(openapi_url="/openapi.json", title=settings.title)
    else:
        logger.error(message="Un Authorized or Error Occurred", functionName="Get ReDoc", fileName="App.py")
        return templates.TemplateResponse("401.html", {"request": request}, status_code=404)


@fastApp.get("/openapi.json", name="Get OpenAPI json", tags=["OpenAPI Specifications"])
async def getOpenApi(request: Request, token: str = Depends(getCookies)):
    if token is not None and len(token) != 0:
        logger.info(message="Getting OpenAPI", functionName="Get OpenAPI", fileName="App.py")
        return get_openapi(title=settings.title, version="1.0.0", routes=fastApp.routes)
    else:
        logger.error(message="Un Authorized or Error Occurred", functionName="Get ReDoc", fileName="App.py")
        return templates.TemplateResponse("401.html", {"request": request}, status_code=404)


@fastApp.get("/redoc", name="Get ReDoc", tags=["OpenAPI Specifications"])
async def getRedoc(request: Request, token: str = Depends(getCookies)):
    if token is not None and len(token) != 0:
        logger.info(message="Getting ReDoc", functionName="Get ReDoc", fileName="App.py")
        return get_redoc_html(openapi_url="/openapi.json", title=settings.title)
    else:
        logger.error(message="Un Authorized or Error Occurred", functionName="Get ReDoc", fileName="App.py")
        return templates.TemplateResponse("401.html", {"request": request}, status_code=404)


Utils.updateSchemaName(app=fastApp, function=internalLogin, name="Internal User Login Schema")
Utils.updateSchemaName(app=fastApp, function=contactUs, name="Contact Us Schema")
