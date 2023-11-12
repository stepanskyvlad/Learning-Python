# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
    while n >= 10:
        n = sum([int(digit) for digit in str(n)])
    return n


def digital_root_1(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n


def digital_root_2(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


print(digital_root(493193))  # 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
