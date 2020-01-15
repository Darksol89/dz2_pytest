"""
Тесты для проверки различных методов у множества
"""

import pytest


@pytest.mark.parametrize('set_element', [4, 7])
def test_adding_element_in_set(create_set, set_element):
    """Тест на добавление элемента в множество."""
    create_set.add(set_element)
    assert set_element in create_set


@pytest.mark.parametrize('set_element', [4, 2, 10])
def test_remove_element_from_set(create_set, set_element):
    """Тест на удаление элемента из множества."""
    create_set.remove(set_element)
    assert not set_element in create_set


def test_update_set(create_set):
    """Тест на объединение двух множеств."""
    new_set = set()
    new_set.update(create_set)
    assert new_set == create_set


def test_clear_all_set(create_set):
    """Тест на удаление всех элементов из множества."""
    create_set.clear()
    assert len(create_set) != 10


@pytest.mark.parametrize('new_element', [2, 8, 14])
def test_compare_sets(create_set, new_element):
    """Тест на сравнение 2-х сетов, дефолтного и с измененными значениями элементов."""
    new_set = create_set.copy()
    create_set.remove(new_element)
    assert new_set != create_set
