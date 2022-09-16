numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

doubled_list = []
for i in numbers_list:
    doubled_list.append(i * 2)

print(doubled_list)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# better way
def double(x):
    return x * 2


doubled_list_functional = list(map(double, numbers_list))
print(doubled_list_functional)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
