"""
Згенерувати матрицю A, m*n з випадкових
елементів, що є цілими числами від 0 до 10. Видалити рядки, які
містять елементи, що повторюються.
"""
from random import randint


m = int(input("Numbers of rows: "))
n = int(input("Numbers of column: "))
matrix = [[randint(0, 10) for _ in range(n)] for _ in range(m)]

print('Created matrix:')
for i in range(m):
    for j in range(n):
        print("{0:^6}".format(matrix[i][j]), end="|")
    print('\n', '-'*7*n)

new_matrix = [i for i in matrix if len(i) == len(set(i))]
print('New matrix:')
for i in range(len(new_matrix)):
    for j in range(n):
        print("{0:^4}".format(new_matrix[i][j]), end='|')
    print('\n', '-'*5*n)
