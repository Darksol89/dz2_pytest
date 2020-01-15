"""
Фикструа для создания тестовой строки
"""
import pytest


@pytest.fixture()
def create_string():
    my_test_string = "It's simple test for work with string!"
    return my_test_string
