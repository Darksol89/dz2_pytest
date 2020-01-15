"""
Тесты на методы работы со строками
"""

import pytest


# Тест на сложение строк
def test_concatanation_strings(create_string):
    my_string = '1223547'
    assert my_string + create_string != create_string


# Тест на проверку длины строк
def test_compare_lenght_strings(create_string):
    assert len(create_string) != create_string * 3


# Тест на доступ по индексу в строке
@pytest.mark.parametrize('index', [0, 2, 10])
def test_acces_to_index_of_string(create_string, index):
    assert create_string[index]


# Тест на разбиение строки по разделителю
@pytest.mark.parametrize('splitter', [' ', '!'])
def test_split_string(create_string, splitter):
    assert create_string != create_string.split(splitter)


# Тест на преобразование строки к верхнему регистру
def test_uppercase_for_string(create_string):
    assert create_string != create_string.upper()
