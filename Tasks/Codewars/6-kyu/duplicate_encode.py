# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
def duplicate_encode(word):
    letter_counter = {}
    for letter in word.lower():
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1

    result_list = [")" if letter_counter[letter] > 1 else "(" for letter in word.lower()]

    return "".join(result_list)


print(duplicate_encode(word="Success"))  # ")())())"
