# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
def count_bits(n):
    return bin(n).count("1", 2)


print(count_bits(1234))  # 10011010010 --> 5 bits
