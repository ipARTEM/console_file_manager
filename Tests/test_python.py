import math
from functions_for_the_test import division



def test_filter_one():
    """
    Функция фильтрации
    :return:
    """
    assert list(filter(lambda x: (x >= 3), (1, 2, 3, 4))) == [3, 4]


def test_division():
    """
    Функция деления
    :return:
    """
    assert division(8, 4) == 2


def test_map():
    """
    Функция map пропускает через lambda функцию итерируемый объект
    :return:
    """
    assert list(map(lambda x: x * 2, [1, 2, 3, 4, 5])) == [2, 4, 6, 8, 10]


def test_sorted():
    """
    Сортировка
    :return:
    """
    assert sorted(['d', '3', 'df', '5', '1', 'b']) == ['1', '3', '5', 'b', 'd', 'df']


def test_math_pi():
    assert math.pi == 3.141592653589793

def test_math_sqrt():
    assert math.sqrt(16) == 4.0

def test_math_pow():
    assert math.pow(5,2) == 25.0

def test_math_hypot():
    assert math.hypot(4,3) == 5.0
