from random import randint


c = 0
m = int(input("Кількість стовпців: "))
n = int(input("Кількість рядків: "))
a = int(input("Нижня границя значень: "))
b = int(input("Верхня границя значень: "))
matrix = [[randint(a, b) for _ in range(n)] for _ in range(m)]

print("Початкова матриця:")
for i in range(n):
    for j in range(m):
        print("{0: ^6}".format(matrix[j][i]), end="|")
        c += matrix[j][i]
    print('\n', '-' * m * 7)

for a in matrix:
    min_mat = min(a)
    index = a.index(min_mat)
    new_elem = round(sum(a)/len(a), 2)
    a.remove(min_mat)
    a.insert(index, new_elem)

print("Змінена матриця(замінили мінімальні значення в кожному стовпці):")
for i in range(n):
    for j in range(m):
        print("{0: ^6}".format(matrix[j][i]), end="|")
        c += matrix[j][i]
    print('\n', '-' * m * 7)
