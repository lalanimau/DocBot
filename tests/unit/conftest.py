import pytest


@pytest.fixture(scope='function', autouse=True)
def mock_settings(monkeypatch):
    class Settings:
        ALIASES = ''

        def __getattr__(self, item):
            return None

    settings = Settings()
    monkeypatch.setattr('docbot.settings', settings)
    monkeypatch.setattr('docbot.dispatcher.settings', settings)
