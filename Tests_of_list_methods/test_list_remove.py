"""
Тест с проверкой удаления определенного элемента из списка
"""
import pytest


@pytest.mark.parametrize(('element'), [2, 5, 7])
def test_remove_item_from_list(create_list, element):
    create_list.remove(element)
    assert len(create_list) < 10
