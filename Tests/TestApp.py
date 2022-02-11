from httpx import AsyncClient
from starlette.testclient import TestClient

from App import fastApp

testClient = TestClient(fastApp)
asyncClient = AsyncClient(app=fastApp, base_url="http://localhost:8000")
