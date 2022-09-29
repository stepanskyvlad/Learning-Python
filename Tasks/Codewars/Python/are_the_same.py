# Given two arrays a and b write a function comp(a, b) (or compSame(a, b)) that checks whether the two arrays have the
# "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears).
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
def comp(array1, array2):
    if array1 is None or array2 is None or (len(array1) != len(array2)):
        return False
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == (array2[j] ** 0.5):
                array2.pop(j)
                break
    return True if not array2 else False


# the best solution
def comp_best(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


print(comp([], []))
