"""
Тесты для проверки различных методов у множества
"""

import pytest


# Тест на добавление элемента в множество
@pytest.mark.parametrize('set_element', [4, 7])
def test_adding_element_in_set(create_set, set_element):
    create_set.add(set_element)
    assert set_element in create_set


# Тест на удаление элемента из множества
@pytest.mark.parametrize('set_element', [4, 2, 10])
def test_remove_element_from_set(create_set, set_element):
    create_set.remove(set_element)
    assert not set_element in create_set


# Тест на объединение двух множеств
def test_update_set(create_set):
    new_set = set()
    new_set.update(create_set)
    assert new_set == create_set


# Тест на удаление всех элементов из множества
def test_clear_all_set(create_set):
    create_set.clear()
    assert len(create_set) != 10


# Тест на сравнение 2-х сетов, дефолтного и с измененными значениями элементов
@pytest.mark.parametrize('new_element', [2, 8, 14])
def test_compare_sets(create_set, new_element):
    new_set = create_set.copy()
    create_set.remove(new_element)
    assert new_set != create_set
