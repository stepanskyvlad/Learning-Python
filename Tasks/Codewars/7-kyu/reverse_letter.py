def reverse_letter(string):
    new_list = [symbol for symbol in string if symbol.isalpha()]
    result = ("".join(new_list))[::-1]
    return result


print(reverse_letter("ultr53o?n"))  # "nortlu"
