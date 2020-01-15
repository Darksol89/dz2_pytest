"""Тесты на методы работы со строками."""

import pytest


def test_concatenation_strings(create_string):
    """Тест на сложение строк."""
    my_string = '1223547'
    assert my_string + create_string != create_string


def test_compare_lenght_strings(create_string):
    """Тест на проверку длины строки."""
    assert len(create_string) != create_string * 3


@pytest.mark.parametrize('index', [0, 2, 10])
def test_acces_to_index_of_string(create_string, index):
    """Тест на доступ по индексу в строке."""
    assert create_string[index]


@pytest.mark.parametrize('splitter', [' ', '!'])
def test_split_string(create_string, splitter):
    """Тест на разбиение строки по разделителю."""
    assert create_string != create_string.split(splitter)


def test_uppercase_for_string(create_string):
    """Тест на преобразование строки к верхнему регистру."""
    assert create_string != create_string.upper()
