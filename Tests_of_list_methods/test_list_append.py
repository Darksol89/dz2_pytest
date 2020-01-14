"""
Тест на  проверку добавления элемента в список и сравнение его длины
"""
import pytest


@pytest.mark.parametrize(('item'), [1, 2, 3])
def test_add_new_item_in_list(create_list, item):
    create_list.append(item)
    print(create_list)
    assert len(create_list) > 10
