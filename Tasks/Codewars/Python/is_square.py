from math import sqrt


def is_square(n):
    if n > 0:
        return n % round(n ** (1 / 2), 3) == 0
    elif n == 0:
        return True
    return False


# another solution
def is_square_1(n):
    return n >= 0 and (n ** 0.5) % 1 == 0


# another solution
def is_square_2(n):
    return n >= 0 and sqrt(n).is_integer()


# another solution
def is_square_3(n):
    return 0 <= n == int(sqrt(n)) ** 2


print(is_square(25))
