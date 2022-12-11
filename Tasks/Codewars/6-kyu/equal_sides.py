# Kata name: Equal Sides Of An Array
# You are going to be given an array of integers. Your job is to take that array and
# find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.
def find_even_index(arr):
    for ind, value in enumerate(arr):
        if sum(arr[:ind]) == sum(arr[ind+1:]):
            return ind
    return -1


print(find_even_index([3, 2, 1, 0, 1, 2, 3]))
