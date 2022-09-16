numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mapping
doubled = [x * 2 for x in numbers_list]
print(doubled)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# mapping and filtering the same time
even = [x * 2 for x in numbers_list if x % 2 == 0]
print(even)  # Output: [0, 4, 8, 12, 16]
