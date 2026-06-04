import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c


async def test_health(client):
    r = await client.get("/health")
    assert r.status_code == 200


async def test_register_and_login(client):
    payload = {"email": "test@example.com", "password": "secret123"}
    r = await client.post("/auth/register", json=payload)
    assert r.status_code == 201

    r = await client.post("/auth/login", data={"username": payload["email"], "password": payload["password"]})
    assert r.status_code == 200
    assert "access_token" in r.json()
