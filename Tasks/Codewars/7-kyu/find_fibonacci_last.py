# Kata name: Find Fibonacci last digit

def get_last_digit(index):
    a, b = 0, 1
    for i in range(0, index):
        a, b = b, a + b
    return int(str(a)[-1])


# other solutions
def get_last_digit_1(index):
    a, b = 0, 1
    for _ in range(index):
        a, b = b, (a+b) % 10
    return a


# the best solutions
def get_last_digit_2(index):
    # it is periodic on 60
    last, tmp, index = 0, 1, index % 60
    for i in range(index):
        last, tmp = tmp, (last + tmp) % 10
    return last


print(get_last_digit(15))
