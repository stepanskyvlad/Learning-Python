# Disemvowel Trolls
def disemvowel(string_):
    return "".join(letter for letter in string_ if letter.lower() not in "aeiou")


# other solutions
def disemvowel_1(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

