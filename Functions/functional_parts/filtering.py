numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = []
for i in numbers_list:
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)  # [0, 2, 4, 6, 8]


def is_even(x):
    return x % 2 == 0


even_numbers_functional = list(filter(is_even, numbers_list))
print(even_numbers_functional)  # [0, 2, 4, 6, 8]
