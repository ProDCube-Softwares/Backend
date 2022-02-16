import pytest

from Tests.App import asyncClient


@pytest.mark.anyio
async def testLogin():
    response = await asyncClient.post("/internalLogin",
                                      data={"email": "vetrichelvan@prodcube.dev", "password": "prodcube2021"})
    assert response.status_code == 303


@pytest.mark.anyio
async def testLoginInvalidPassword():
    response = await asyncClient.post("/internalLogin",
                                      data={"email": "vetrichelvan@prodcube.dev", "password": "password"})
    assert response.status_code == 404


@pytest.mark.anyio
async def testLoginInvalidUser():
    response = await asyncClient.post("/internalLogin",
                                      data={"email": "test@prodcube.dev", "password": "password"})
    assert response.status_code == 404
