# Kata name: List Filtering

def is_num(x):
    return isinstance(x, int)


def filter_list(lst):
    return list(filter(is_num, lst))


print(filter_list([0, 1, 2, 'aasf', '1', '123', 123]))
