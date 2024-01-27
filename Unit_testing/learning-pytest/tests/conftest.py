import pytest
import source.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def another_rectangle():
    return shapes.Rectangle(5, 6)