# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def array_diff(a: list, b: list):
    new_list = a.copy()
    for i in a:
        if i in b:
            new_list.remove(i)
    return new_list


print(array_diff([1, 1, 1, 2, 2, 2, 3], [1, 2]))
