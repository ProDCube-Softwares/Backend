import pytest

from Tests.TestApp import asyncClient


@pytest.mark.anyio
async def testContactUs():
    response = await asyncClient.post("/contact-us",
                                      json={"name": "Test", "email": "", "message": "Test", "contact": "Test",
                                            "country": "IN", "region": "Test"})
    assert response.status_code == 200
