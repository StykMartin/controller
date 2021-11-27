import pytest
from starlette.testclient import TestClient


@pytest.fixture(scope="function")
def client():
    from controller.main import app

    client = TestClient(app)

    return client
