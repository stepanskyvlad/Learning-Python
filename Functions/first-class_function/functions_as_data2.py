import math


def double(x):
    return x * 2


def minus_one(x):
    return x - 1


def squared(x):
    return x * x


function_list = [
    squared,
    double,
    minus_one,
    math.sqrt,

]

my_number = 3

for func in function_list:
    my_number = func(my_number)
    print(my_number)


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)
