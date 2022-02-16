import pytest

from Tests.App import asyncClient


@pytest.mark.anyio
async def testContactUs():
    response = await asyncClient.post("/contact-us",
                                      json={"name": "Test", "email": "vetrichelvan@prodcube.com", "message": "Test"})
    assert response.status_code == 200
