"""
У створеному випадковим чином списку цілих чисел видалити ті
елементи, які зустрічаються більше, ніж двічі. Створити списки,
відсортовані за зростанням та за спаданням. З даних списків
сформувати третій список, кожен елемент якого дорівнює
середньому геометричному двох попередніх елементів, які
знаходяться на однаковому зсуві.
"""
import random
from collections import Counter
a = int(input("Згенерувати послідовність чисел від: " ))
b = int(input("До: "))
c = int(input("Кількість елементів в списку: "))
arr = [random.randint(a, b) for i in range(c)]
print(f"Згенерований список: \n{arr}")

set1 = set(arr)
arr1 = [k for k, v in Counter(arr).items() if v > 2]
set2 = set(arr1)

arr2 = set1.difference(set2)
print(f"\nСписок без повторюваних елементів \n{arr2}")

asc_sort = sorted(arr2)
desc_sort = sorted(arr2, reverse=True)
print(f"\nВідсортовані списки за зростанням і спаданням:\n{asc_sort} \n{desc_sort}")

new_arr3 =[(a[0]*a[1])**(1/2) for a in list(zip(asc_sort,desc_sort))]
print(f"Третій список: \n{new_arr3}")
