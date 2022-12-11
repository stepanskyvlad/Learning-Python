# Kata name: Factorial

# My two solutions
from math import factorial
def factorial_0(n):  # max n -> 998
    if n == 1:
        return n
    return n * factorial_0(n - 1)


def factorial_1(n):  # max n -> 1558
    result = 1
    while n:
        result *= n
        n -= 1
    return result


# other solutions
def factorial_2(n):
    j = 1
    for i in range(1, n + 1):
        j *= i
    return j


def factorial_3(n):
    if n > 1:
        return n * factorial_3(n - 1)
    return 1


# another task
def factorial_4(n):
    if n < 0 or n > 12:
        raise ValueError("Error")
    elif n > 1:
        return n * factorial_4(n-1)
    return 1


print(factorial_2(1558))
print(factorial(1558))
