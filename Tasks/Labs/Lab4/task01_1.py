"""Випадковим чином створити два цілочисельних списки. Сформувати
новий список, на парних місцях якого будуть елементи з непарними
індексами з першого списку, а на непарних – з парними індексами з
другого. Сформувати з нового списку вдвічі коротший список з
випадковими елементами. Перетворити цей список на рядок."""
from random import *

amount = int(input("Enter the amount of numbers in the lists --> "))
max_number = int(input("Enter the max number in the lists --> "))

# Сформувати випадковим чином два списки
first_list = sample(range(max_number), amount)
second_list = sample(range(max_number), amount)
print(f"\tFirst list:\n{first_list}\n\tSecond list\n{second_list}")

# Новий список на парних місцях непарні числа першого списку,
# на непарних місцях парні числа другого списку
new_list = first_list[1::2]
x = 1
for i, k in enumerate(second_list[::2]):
    new_list.insert(i+x, k)
    x += 1
print(f"\tThe new list has been created:\n{new_list}")

short_list = sample(new_list, round(len(new_list)/2))
print(f"\tThe short list has been created:\n{short_list}")

my_string = ''
for i in short_list:
    my_string += str(i)
print(f"\tThe string has been created:\n{my_string}")
