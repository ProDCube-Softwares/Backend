from httpx import AsyncClient
from starlette.testclient import TestClient

from App import fastApp
from Utils import Environment

testSettings = Environment().generateSettings()
testClient = TestClient(fastApp)
asyncClient = AsyncClient(app=fastApp, base_url="http://localhost:8000")
