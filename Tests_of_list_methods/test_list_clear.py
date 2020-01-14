"""
Тест на удаление всех элементов из списка
"""


def test_remove_all_elements_from_list(create_list):
    create_list.clear()
    assert len(create_list) != 10
