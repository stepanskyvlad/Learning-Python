# [[1, 2], [5, 6]]
# [[3, 4], [1, 2]]
# [[4, 6], [6, 8]]

def a_b(a, b):
    my_list = []
    if len(a) == len(b):
        for i, j in zip(a, b):
            list1 = []
            for x, y in zip(i, j):
                z = x + y
                list1.append(z)
                print(list1)
            my_list.append(list1)
    else:
        raise ValueError('There is not equal lists')
    return my_list


my = a_b([[1, 2], [5, 6], [7, 8]], [[3, 4], [1, 2], [2, 1]])
print(my)
