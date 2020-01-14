"""
Тест на проверку неравенства нового отсортироанного списка и старого списка
"""

import pytest


def test_sorting_elements_in_list(create_list):
    for element in range(15):
        create_list.append(element)
    new_lst = sorted(create_list)
    assert new_lst != create_list
