def invert(lst):
    return [-i for i in lst]


# another solution
def invert_another(lst):
    return list(map(lambda x: -x, lst))


print(invert([1,2,3,4,5]))
