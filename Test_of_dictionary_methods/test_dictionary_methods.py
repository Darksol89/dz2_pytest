"""
Тесты на методы словаря
"""

import pytest

# Тест на удаление значений из словаря
@pytest.mark.parametrize('value', [4, 2, 10])
def test_remove_element_from_dict(create_dictionary, value):
    create_dictionary.pop(value)

    assert not value in create_dictionary

@pytest.mark.parametrize('key', 'value', [(1), (2)])
def test_check_element_in_dict(create_dictionary, key, value):
    create_dictionary.items(key, value)
    assert value in create_dictionary