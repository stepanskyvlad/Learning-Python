# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    return " ".join(map(lambda x: x[::-1] if len(x) >= 5 else x, sentence.split(" ")))


print(spin_words("Hey fellow warriors"))  # "Hey wollef sroirraw"
