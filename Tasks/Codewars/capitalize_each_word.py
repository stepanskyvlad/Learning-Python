from string import capwords


def to_jaden_case_another(my_string):
    return capwords(my_string)


def to_jaden_case(my_string):
    b = []
    for temp in my_string.split(' '):
        b.append(temp.capitalize())
    return ' '.join(b)


print(to_jaden_case("I'm ukrainian. I'm from ukraine'"))
print(to_jaden_case_another("I'm ukrainian. I'm from ukraine'"))

