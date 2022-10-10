# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
def find_it(seq):
    for i in set(seq):
        if seq.count(i) % 2:
            return i


print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
