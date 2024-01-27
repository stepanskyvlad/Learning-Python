import pytest


def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle):
    # rectangle = shapes.Rectangle(10, 20)
    rectangle = my_rectangle
    assert rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_not_equal(my_rectangle, another_rectangle):
    assert my_rectangle != another_rectangle
