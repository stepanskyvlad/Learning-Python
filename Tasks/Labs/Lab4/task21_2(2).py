"""
Згенерувати матрицю A розмірністю m*n з випадкових
елементів, що є цілими числами. Замінити мінімальний елемент
у кожному стовпці на середнє арифметичне рядка, який містить
даний мінімальний елемент.
"""
import random
a = int(input("Згенерувати послідовність чисел від: " ))
b = int(input("До: "))
m = int(input("Розмір матриці: рядки: "))
n = int(input("Стовпці: "))
matrix = []
for i in range(m):
    arr = [random.randint(a, b) for j in range(n)]
    matrix.append(arr)
for a in matrix:
    print(a)
print()

for a in matrix:
    min_mat = min(a)
    indx = a.index(min_mat)
    new_elem = sum(a)/len(a)
    a.remove(min_mat)
    a.insert(indx, new_elem)
    print(a)
