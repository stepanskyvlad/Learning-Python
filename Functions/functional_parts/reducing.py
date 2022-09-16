from functools import reduce


numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_sum(acc, x):
    print(f"acc is {acc}, x is {x}")
    return acc + x
# OUTPUT:
# acc is 10, x is 0
# acc is 10, x is 1
# acc is 11, x is 2
# acc is 13, x is 3
# acc is 16, x is 4
# acc is 20, x is 5
# acc is 25, x is 6
# acc is 31, x is 7
# acc is 38, x is 8
# acc is 46, x is 9


sum_of_list = reduce(get_sum, numbers_list, 10)  # <- last number is optional
print(sum_of_list)  # 55
