# Kata name: Maximum subarray sum

from math import inf


def max_sequence(arr):
    max_so_far = -inf
    max_ending_here = 0
    for i in arr:
        max_ending_here += i
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far if max_so_far > 0 else 0


# other solution
def max_sequence_1(arr):
    current = 0
    max_found = 0

    for value in arr:
        current += value
        if current < 0:
            current = 0

        if current > max_found:
            max_found = current

    return max_found


def max_sequence_2(arr):
    best = cur = 0
    for i in arr:
        cur = max(cur + i, 0)
        best = max(best, cur)
    return best


print(max_sequence([1, -3, 4, -1, 2, 1, -5, 4]))
