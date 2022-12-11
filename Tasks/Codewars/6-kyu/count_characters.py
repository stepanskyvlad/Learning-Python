# Kata name: Count characters in your string

def count(string):
    result_dict = {}
    for i in string:
        result_dict.setdefault(i, 0)
        result_dict[i] += 1
    return result_dict


# other solutions
def count_1(string):
    ret = {}
    for char in string:
        ret[char] = ret.get(char, 0) + 1
    return ret


print(count('aba'))
