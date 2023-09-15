"""
Випадковим чином створити цілочисельний список. Визначте індекси
найбільшого з непарних за значенням додатних елементів та
найбільшого з парних за значенням додатних елементів. Знайдіть
індекс елемента, найближчого за значенням до різниці двох
попередніх елементів. Видаліть цей елемент, а також сформуйте
новий список з тих елементів, що у сумі з виведеним перевищують
число 10 .
"""
import random

num_of_int = int(input("Enter a number of integers --> "))
max_num = int(input("Enter the max number of the list --> "))

my_list = random.sample(range(max_num+1), num_of_int)

max_even = max([i for i in my_list if i % 2 == 0])
max_odd = max([i for i in my_list if i % 2 != 0])

index_max_even = my_list.index(max_even)
index_max_odd = my_list.index(max_odd)

print(f"Created list:\n{my_list}\nMax even number and its index -- > "
      f"{max_even}({index_max_even})\nMax odd number and its index --> "
      f"{max_odd}({index_max_odd})")

difference = abs(max_odd-max_even)
print(f"The difference between max numbers -> {difference}")

near_dif = max(my_list)
for i in my_list:
    if abs(i-difference) < near_dif:
        near_dif = i
index_near_dif = my_list.index(near_dif)
print(f"The number near the difference and its index -> {near_dif}({index_near_dif})")

popped_num = my_list.pop(index_near_dif)
new_list = [i for i in my_list if i + popped_num > 10]
print(f"New list:\n{new_list}")
