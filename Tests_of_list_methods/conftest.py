"""
Фикстура для создания списка в 10 элементов
"""
import pytest


@pytest.fixture()
def create_list():
    lst = list(range(10))
    return lst
