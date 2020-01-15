"""
Тесты на методы словаря
"""

import pytest


# Тест на удаление значений из словаря
@pytest.mark.parametrize('value', [4, 2, 7])
def test_remove_element_from_dict(create_dictionary, value):
    create_dictionary.pop(value)
    assert not value in create_dictionary


# Тест на возвращение ключа в словаре
@pytest.mark.parametrize('value', [0, 1, 2])
def test_check_key_in_dictionary(create_dictionary, value):
    assert create_dictionary.get(value) in create_dictionary


# Тест на сравнение 2-х словарей. Пустой и не пустой
def test_clear_dictionary(create_dictionary):
    new_dict = create_dictionary.copy()
    create_dictionary.clear()
    assert new_dict != create_dictionary


# Тест на добавление ключа-значения в словарь. И сравнение 2-х словарей
def test_modified_dictionary(create_dictionary):
    old_dict = create_dictionary.copy()
    create_dictionary.setdefault(20, 0)
    assert old_dict != create_dictionary


# Тест на проверку наличия ключей в словаре
@pytest.mark.parametrize('keys', [0, 1, 2])
def test_return_keys_in_dictionary(create_dictionary, keys):
    assert keys in create_dictionary.keys()
