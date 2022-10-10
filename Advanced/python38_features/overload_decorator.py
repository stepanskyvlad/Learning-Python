# перенавантаження методів - коли ми маємо хоча б два методи з однаковим ім'ям, але відрізняються аргументи по типам
from typing import Union, Literal, overload


def parse_roman(roman):
    return 'roman'


def convert_to_roman(num):
    return num


@overload
def add(x: str, y: str, to_arabic: Literal[True]) -> int: ...


@overload
def add(x: str, y: str, to_arabic: Literal[False]) -> str: ...


def add(x: str, y: str, to_arabic: bool) -> Union[str, int]:
    a = parse_roman(x)
    b = parse_roman(y)

    c = a + b
    return c if to_arabic else convert_to_roman(c)


result = add('1', '11', False)  # we'll get a string type

r = result / 3  # -> Expected type 'int', got 'str' instead
