import pytest
import sys

sys.path.append('.')
from api import app

@pytest.fixture
def api():
    api = app
    return api

@pytest.fixture
def client():
    api = app
    client = api.test_client()
    yield client
