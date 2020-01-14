"""
Тест на сравнение 2-х списков с правильным\неправильным порядком элементов
"""

import pytest


def test_reverse_elements_in_list(create_list):
    new_list = []
    for element in create_list:
        new_list.append(element)
    create_list.reverse()

    assert new_list != create_list
