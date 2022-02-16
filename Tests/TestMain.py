import pytest
from starlette.testclient import TestClient

from App import fastApp, getCookies
from Database import Connection
from Tests.App import testSettings

Connection(databaseName="ProDCubeTesting", host=testSettings.databaseUrl, port=int(testSettings.databasePort)).connect()
testClient = TestClient(fastApp)


def mockGetCookies():
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVmV0cmljaGVsdmFuIiwiZW1haWwiOiJ2ZXRyaWNoZWx2YW5Ac" \
           "HJvZGN1YmUuZGV2Iiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjQ0OTU0MTcwfQ.3JizmNOvvxmKNQA00YRJHhZ2oJa0vX-B07whGnZPBX4"


fastApp.dependency_overrides[getCookies] = mockGetCookies


@pytest.mark.anyio
def testMain() -> None:
    print("Testing Main")
    response = testClient.request("GET", "/")
    assert response.status_code == 200


# @pytest.mark.anyio
# def testDocumentationUnAuthorized() -> None:
#     response = testClient.request("GET", "/docs")
#     assert response.status_code == 404
#
#
# @pytest.mark.anyio
# def testOpenAPIUnAuthorized() -> None:
#     response = testClient.request("GET", "/openapi.json")
#     assert response.status_code == 404
#
#
# @pytest.mark.anyio
# def testReDocUnAuthorized() -> None:
#     response = testClient.request("GET", "/redoc")
#     assert response.status_code == 404


@pytest.mark.anyio
def testDocumentation() -> None:
    response = testClient.request("GET", "/docs")
    assert response.status_code == 200


@pytest.mark.anyio
def testOpenAPI() -> None:
    response = testClient.request("GET", "/openapi.json")
    assert response.status_code == 200


@pytest.mark.anyio
def testReDoc() -> None:
    response = testClient.request("GET", "/redoc")
    assert response.status_code == 200
