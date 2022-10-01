# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative
# numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    num_of_positives = len(list(filter(lambda x: x > 0, arr)))
    sum_of_negatives = sum(list(filter(lambda x: x < 0, arr)))
    return [num_of_positives, sum_of_negatives]


# another solution
def count_positives_sum_negatives_1(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []


print(count_positives_sum_negatives([]))
