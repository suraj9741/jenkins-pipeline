import pytest
from app import app as test_app


@pytest.fixture()
def app():
    with test_app.app_context():
        yield test_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def mock_sleep(monkeypatch):
    def sleep(secs):
        pass

    monkeypatch.setattr("app.sleep", sleep)
