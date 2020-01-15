"""Тесты на методы работы со словарём."""

import pytest


@pytest.mark.parametrize('value', [4, 2, 7])
def test_remove_element_from_dict(create_dictionary, value):
    """Тест на удаление значений из словаря."""
    create_dictionary.pop(value)
    assert not value in create_dictionary


@pytest.mark.parametrize('value', [0, 1, 2])
def test_check_key_in_dictionary(create_dictionary, value):
    """Тест на возвращение ключа в словаре."""
    assert create_dictionary.get(value) in create_dictionary


def test_clear_dictionary(create_dictionary):
    """Тест на сравнение 2-х словарей. Пустой и не пустой."""
    new_dict = create_dictionary.copy()
    create_dictionary.clear()
    assert new_dict != create_dictionary


def test_modified_dictionary(create_dictionary):
    """Тест на добавление ключа-значения в словарь. И сравнение 2-х словарей."""
    old_dict = create_dictionary.copy()
    create_dictionary.setdefault(20, 0)
    assert old_dict != create_dictionary


@pytest.mark.parametrize('keys', [0, 1, 2])
def test_return_keys_in_dictionary(create_dictionary, keys):
    """Тест на проверку наличия ключей в словаре."""
    assert keys in create_dictionary.keys()
