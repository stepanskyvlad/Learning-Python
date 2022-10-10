# Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
def order(sentence):
    wordlist = sentence.split()
    new_list = []
    for word in wordlist:
        for letter in word:
            if letter.isdigit():
                new_list.append((int(letter), word))
                break
    new_string = ' '.join([i[1] for i in sorted(new_list)])
    return new_string


print(order("is2 Thi1s T4est 3a"))
