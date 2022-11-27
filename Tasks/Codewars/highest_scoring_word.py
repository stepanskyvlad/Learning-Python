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


print(high("man i need a taxi up to ubud"))
