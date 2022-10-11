# перенавантаження методів - коли ми маємо хоча б два методи з однаковим ім'ям, але відрізняються аргументи по типах
from typing import Union, Literal, overload


def parse_roman(roman):
    value = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    last, func_result = 0, 0
    for char in list(roman)[::-1]:
        if last == 0:
            func_result += value[char]
        elif last > value[char]:
            func_result -= value[char]
        else:
            func_result += value[char]
        last = value[char]
    return func_result


def convert_to_roman(num):
    values = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
              50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    convert_list = []
    for value in values.keys():
        while num >= value:
            num -= value
            convert_list.append(values[value])
    return ''.join(convert_list)


@overload
def add(x: str, y: str, to_arabic: Literal[True]) -> int: ...


@overload
def add(x: str, y: str, to_arabic: Literal[False]) -> str: ...


def add(x: str, y: str, to_arabic: bool) -> Union[str, int]:
    a = parse_roman(x)
    b = parse_roman(y)

    c = a + b
    return c if to_arabic else convert_to_roman(c)


result = add('IV', 'XXXIV', to_arabic=False)  # we'll get a string type
print(result)
try:
    r1 = result / 3  # -> Expected type 'int', got 'str' instead
except Exception as ex:
    print(f"There's error - {ex}")

result = add('VIII', 'IV', to_arabic=True)  # we'll get an int type
print(result)
print(r2 := result / 3)
