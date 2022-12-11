# Kata name: Correct the mistakes of the character recognition software

# Correct the mistakes of the character recognition software
def correct(s):
    s = s.replace('5', 'S')
    s = s.replace('0', 'O')
    s = s.replace('1', 'I')
    return s


# other solutions
def correct_1(string):
    return string.translate(str.maketrans("501", "SOI"))


def correct_2(string):
    return string.replace('1', 'I').replace('0', 'O').replace('5', 'S')


def correct_3(s):
    mapping = str.maketrans({'0': 'O', '1': 'I', '5': 'S'})
    return s.translate(mapping)


def correct_4(string):
    tr = str.maketrans('015', 'OIS')
    return string.translate(tr)
