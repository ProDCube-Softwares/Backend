import pytest
from starlette.testclient import TestClient

from App import fastApp

testClient = TestClient(fastApp)


@pytest.mark.anyio
def testMain():
    response = testClient.request("GET", "/")
    assert response.status_code == 200
