"""Фикстуры для работы с различными структурами данных."""

import pytest


@pytest.fixture()
def create_dictionary():
    """Функция для создания словаря."""
    my_dict = {a: a ** 2 for a in range(8)}
    return my_dict


@pytest.fixture()
def create_list():
    """Функция для создания списка."""
    lst = list(range(10))
    return lst


@pytest.fixture()
def create_set():
    """Функция для создания множества."""
    my_set = {i * 2 for i in range(10)}
    return my_set


@pytest.fixture()
def create_string():
    """Функция для создания строки."""
    my_test_string = "It's simple test for work with string!"
    return my_test_string
