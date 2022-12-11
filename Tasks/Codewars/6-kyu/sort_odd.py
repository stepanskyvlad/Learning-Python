# Kata name: Sort the odd

# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving
# the even numbers at their original positions. [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
def sort_array(source_array):
    # create sorted list with odds
    odd_list = sorted(list(filter(lambda x: x % 2 != 0, source_array)), reverse=True)
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd_list.pop()
    return source_array


# another solution
def sort_array_1(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]


# another solution
def sort_array_2(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]


# test my solution
def test_sort_array():
    return_value = sort_array([2, 22, 37, 11, 4, 1, 5, 0])
    assert return_value == [2, 22, 1, 5, 4, 11, 37, 0]
