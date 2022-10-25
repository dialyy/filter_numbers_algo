import pytest

from app import create_app


@pytest.fixture
def client():
    test_app = create_app()
    test_app.config['TESTING'] = True
    client = test_app.test_client()

    yield client
