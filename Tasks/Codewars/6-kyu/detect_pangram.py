# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
def is_pangram(s):
    only_letters = [letter for letter in s.lower() if letter.isalpha()]
    lowercase_string = "abcdefghijklmnopqrstuvwxyz"
    for letter in lowercase_string:
        if letter not in only_letters:
            return False

    return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
