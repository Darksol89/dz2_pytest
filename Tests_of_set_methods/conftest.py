import pytest

@pytest.fixture()
def create_set():
    my_set = {i * 2 for i in range(10)}
    return my_set