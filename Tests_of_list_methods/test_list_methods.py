"""
Тесты на различные методы работы со списком
"""
import pytest


# Тест на  проверку добавления элемента в список и сравнение его длины
@pytest.mark.parametrize(('item'), [1, 2, 3])
def test_add_new_item_in_list(create_list, item):
    create_list.append(item)
    print(create_list)
    assert item in create_list


# Тест с проверкой удаления определенного элемента из списка
@pytest.mark.parametrize(('element'), [2, 5, 7])
def test_remove_item_from_list(create_list, element):
    create_list.remove(element)
    assert not element in create_list


# Тест на удаление всех элементов из списка
def test_remove_all_elements_from_list(create_list):
    create_list.clear()
    assert len(create_list) != 10


# Тест на сравнение 2-х списков с правильным\неправильным порядком элементов
def test_reverse_elements_in_list(create_list):
    new_list = []
    for element in create_list:
        new_list.append(element)
    create_list.reverse()
    assert new_list != create_list


# Тест на проверку неравенства нового отсортироанного списка и старого списка
def test_sorting_elements_in_list(create_list):
    for element in range(15):
        create_list.append(element)
    new_lst = sorted(create_list)
    assert new_lst != create_list
