import pytest

from Tests.TestApp import asyncClient


@pytest.mark.anyio
async def testLogin():
    response = await asyncClient.post("/internalLogin",
                                      data={"email": "vetrichelvan@prodcube.dev", "password": "prodcube2021"})
    assert response.status_code == 303
