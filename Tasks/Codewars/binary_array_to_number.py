def binary_array_to_number(arr):
    return int(''.join(map(str, arr)), 2)


print(binary_array_to_number([1, 0, 1, 0, 1]))
