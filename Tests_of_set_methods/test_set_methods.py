"""
Тесты для проверки различных методов у множества
"""

import pytest


# Тест на добавление элемента в множество
@pytest.mark.parametrize('set_element', [4, 7])
def test_adding_element_in_set(create_set, set_element):
    create_set.add(set_element)
    assert len(create_set) > 10


# Тест на удаление элемента из множества
@pytest.mark.parametrize('set_element', [4, 7, 10])
def test_remove_element_from_set(create_set, set_element):
    create_set.remove(set_element)
    assert len(create_set) > 8
