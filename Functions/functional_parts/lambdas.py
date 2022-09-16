numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

doubled_numbers = list(map(lambda x: x * 2, numbers_list))
print(doubled_numbers)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


def create_multiplier(a):
    return lambda x: x * a


triple = create_multiplier(3)
print(triple(5))  # Output: 15

# sorting using lambda
my_list = [{'num': 3}, {'num': 2}, {'num': 1}]
print(sorted(my_list, key=lambda x: x['num']))
# Output: [{'num': 1}, {'num': 2}, {'num': 3}]
