import pytest


@pytest.fixture(scope="function", autouse=True)
def db():
    print("\nStart DB")
    yield
    print("\nEnd DB")
