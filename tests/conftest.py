import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--base_url", action="store", default="https://reqres.in", help="Type base url"
    )


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption("--base_url")
