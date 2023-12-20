import os
from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from ProjectFastAPI.database import database

# from ProjectFastAPI.routers.post import comment_table, post_table 


os.environ["ENV_STATE"] = "test"

from ProjectFastAPI.database import database  # noqa E402
from ProjectFastAPI.main import app  # noqa E402


@pytest.fixture(scope="session")
def anyio_backed(): 
    return "asyncio"


@pytest.fixture()
def client() -> Generator: 
    yield TestClient(app)


@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator: 
    await database.connect()
    yield
    await database.disconnect()


@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac: 
        yield ac