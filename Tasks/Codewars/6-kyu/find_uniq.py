# Kata name: Find the unique number

# There is an array with some numbers. All numbers are equal except for one. Try to find it!
def find_uniq(arr):
    return [n for n in set(arr) if arr.count(n) == 1][0]


# another solution
def find_uniq_another(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
