import random


def middle(a, b):
    return (a+b)/2


lines = int(input("Enter a number of lines: "))
columns = int(input("Enter a number of columns: "))
i = 0
matrix_A = []
matrix_B = []
while i < lines*columns:
    i += 1
    matrix_A.append(random.randint(1, 1000))
    matrix_B.append(random.randint(1, 1000))
list_1 = list(map(middle, matrix_A, matrix_B))
print("Matrix_A= ", [matrix_A[i*columns:(i+1)*columns] for i in range(lines)])
print("Matrix_B= ", [matrix_B[i*columns:(i+1)*columns] for i in range(len(matrix_B) // columns)])
print("Matrix_C= ", [list_1[i*columns:(i+1)*columns] for i in range(len(list_1) // columns)])
