# Kata name: Delete occurrences of an element if it occurs more than n times

# Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
# For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next
# [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
from collections import defaultdict


def delete_nth(order, max_e):
    new_order = []
    duplications = dict()
    for x in order:
        duplications.setdefault(x, 0)
        duplications[x] += 1
        if duplications[x] <= max_e:
            new_order.append(x)
    return new_order


# other solutions
def delete_nth_1(order, max_e):
    d = {}
    res = []
    for item in order:
        n = d.get(item, 0)
        if n < max_e:
            res.append(item)
            d[item] = n + 1
    return res


def delete_nth_2(order, max_e):
    dct = defaultdict(int)
    res = []
    for i in order:
        dct[i] += 1
        if dct[i] <= max_e:
            res.append(i)
    return res


print(delete_nth_2([1, 2, 3, 1, 2, 1, 2, 3], 2))
