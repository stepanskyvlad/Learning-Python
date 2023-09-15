from random import randint

ssom = []
sum = 0
m = int(input ("Кількість рядків: "))
n = int(input ("Кількість стовпців: "))
a = int(input("Нижня границя значень: "))
b = int(input("Верхня границя значень: "))
bilsh = 0
mass = [[randint(a, b) for _ in range(n)] for _ in range(m)]
for i in range(n):
    for j in range(m):
        print("{0: ^6}".format(mass[i][j]), end="|")
        sum += mass[i][j]
    print('\n', '-' * n * 7)
    ssom.append(sum)
    sum = 0
print()

for i in range(n):
    for j in range(m):
        if bilsh < mass[i][j]:
            bilsh = mass[i][j]
    indstb = int((mass[i].index(bilsh)))
    mass[i][indstb] = round(ssom[indstb] / n, 1)
    bilsh = 0

for i in range(n):
    for j in range(m):
        print("{0: ^6}".format(mass[i][j]), end="|")
    print('\n', '-' * n * 7)

