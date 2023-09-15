"""
Випадковим чином створити два списки дійсних чисел. Визначити
максимальні елементи в кожному списку і поміняти їх місцями.
"""
import random

first_number = random.randint(1, 50)
second_number = random.randint(1, 50)

create_list = [[i] for i in range(0, random.randint(1, first_number))]
create_list1 = [[j] for j in range(0, random.randint(1, second_number))]

random.shuffle(create_list)
random.shuffle(create_list1)

index_max1 = create_list.index(max(create_list))
index_max2 = create_list1.index(max(create_list1))

max_valuable1 = max(create_list)
max_valuable2 = max(create_list1)

print(create_list, "\n", "\b{}".format(create_list1))
print("Index 1: ", index_max1, "\nIndex 2: ", index_max2)

create_list.pop(index_max1)
create_list.insert(index_max1, max_valuable2)

create_list1.pop(index_max2)
create_list1.insert(index_max2, max_valuable1)

print("First list:\n{0}\nSecond list:\n{1}".format(create_list, create_list1))
