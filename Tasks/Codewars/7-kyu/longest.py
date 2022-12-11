# Kata name: Two to One

# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible,\
# containing distinct letters - each taken only once - coming from s1 or s2.
def longest(a1, a2):
    return ''.join(sorted(set(a1).union(set(a2))))


# another solution
def longest_1(a1, a2):
    return "".join(sorted(set(a1 + a2)))


print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))
