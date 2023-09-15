"""
Випадковим чином створити список X , який складається з
елементів цілого типу. Розрахувати елементи списку Y. за
формулою cos ... . Сформувати третій список з
упорядкованих за спаданням значень з обох списків. Вибрати із
сформованого списку випадковим чином два елементи і визначити,
чи входять вони у список X.
"""
import random
import math

num_of_digits = int(input("Enter the number of integers in the list: "))
max_num = int(input("Enter max number of integers: "))

x_list = random.sample(range(max_num+1), num_of_digits)
print(f"List X:\n{x_list}")


def formula(x, my_list):
    x_index = my_list.index(x)+1
    y = math.cos(x**2) + 2.97*(math.log10(x_index**2))**2
    return round(y, 2)


y_list = [formula(i, x_list) for i in x_list]
print(f"List Y:\n{y_list}")

new_list = sorted(x_list+y_list, reverse=True)
print(f"Have created a new reverse list:\n{new_list}")
ran_choices = random.sample(new_list, 2)
print(f"Have chosen two random numbers:\n{ran_choices}")

for i in ran_choices:
    if i in x_list:
        print(f"Number {i} is in X list")
    else:
        print(f"Number {i} isn't in X list")
