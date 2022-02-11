import pytest
from starlette.testclient import TestClient

from App import fastApp, getCookies

testClient = TestClient(fastApp)


def mockGetCookies():
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVmV0cmljaGVsdmFuIiwiZW1haWwiOiJ2ZXRyaWNoZWx2YW5AcHJvZGN1" \
           "YmUuZGV2Iiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjQ0NjAzMTM4fQ.ikPfzXgx2m4YEotHYKUFG5prNIJka7YgcQdf0ECMoOI"


fastApp.dependency_overrides[getCookies] = mockGetCookies


@pytest.mark.anyio
def testMain() -> None:
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
