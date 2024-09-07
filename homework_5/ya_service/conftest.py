import pytest


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status-code")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
    )
    parser.addoption(
        "--status-code",
        default=200,
        type=int,
    )
