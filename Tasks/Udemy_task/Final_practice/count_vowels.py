def count_vowels(user_string):
    vowels_string = 'aeiou'
    counter = 0
    for letter in user_string:
        if letter in vowels_string:
            counter += 1
    return counter


# another solution
def count_vowels_1(txt):
    return sum([1 for x in txt.lower() if x in "aeiou"])
