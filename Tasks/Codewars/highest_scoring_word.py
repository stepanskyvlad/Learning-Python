# Highest Scoring Word
def high(x):
    alphabet = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1, 27)))  # create an alphabet
    wordlist = x.lower().split()  # convert string into list with words
    max_cost = 0  # variable for checking cost of each word
    high_word = ''  # the required word will be written here
    for word in wordlist:
        word_cost = 0
        for letter in word:
            word_cost += alphabet[letter]
        if word_cost > max_cost:
            max_cost = word_cost
            high_word = word
    return high_word


# other solutions
# it's not necessary to build a list of the alphabet.
# you can use the function ord(chr) to get the ascii value
# of a chr and subtract 96 from it because a = 97, b = 98 and so on.
def high_1(x):
    highest_word = ''
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c) - 96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word

    return highest_word


def high_2(x):
    words = x.split(' ')
    score_list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        score_list.append(scores)
    return words[score_list.index(max(score_list))]


print(high_1("man i need a taxi up to ubud"))
