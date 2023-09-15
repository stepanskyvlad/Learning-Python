"""
Випадковим чином створити список дійсних чисел. Визначити
різницю між сумою елементів з парними індексами і сумою елементів,
індекси яких кратні трьом. Вставити цю різницю в кінець списку.
"""
import random


amount_of_nums = int(input("Enter the amount of numbers --> "))
max_num = float(input("Enter the max number of list --> "))
n = 0
my_list = []
while amount_of_nums > n:
    my_list.append(round(random.uniform(0, max_num), 3))
    n += 1

print(my_list)
difference = sum(my_list[::2]) - sum(my_list[3::3])
my_list.append(difference)
print(my_list)
