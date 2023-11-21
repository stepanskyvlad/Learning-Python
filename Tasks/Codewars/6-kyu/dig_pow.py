# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
def dig_pow(n, p):
    result = 0
    for digit, power in zip(str(n), range(p, len(str(n)) + p + 1)):
        result += int(digit)**power

    if (result/n).is_integer():
        return result//n

    return -1


print(dig_pow(46288, 3))  # 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
