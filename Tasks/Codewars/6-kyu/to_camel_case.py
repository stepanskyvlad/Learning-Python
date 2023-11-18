# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
import re


def to_camel_case(text):
    words = re.split(r'_|-', text)
    return ''.join(word.capitalize() if words.index(word) != 0 else word for word in words)


print(to_camel_case("the_stealth_warrior"))  # "theStealthWarrior"
