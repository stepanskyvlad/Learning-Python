import math

square = 0
circle = 0
while square <= 0 or circle <= 0:
    square = float(input("Enter area of the square: "))
    circle = float(input("Enter area of the circle: "))
# Знаходимо сторону і діагональ квадрата
a = math.sqrt(square)
diagonal = math.sqrt(2 * a ** 2)
# Знаходимо радіус кола
r = math.sqrt(circle / math.pi)

if r < a / 2:
    print('Коло поміститися в квадраті')
elif r == a / 2:
    print('Коло є вписаним в квадрат')
else:
    print("Коло не поміститься в квадраті")

if diagonal / 2 < r:
    print('Квадрат поміститься в колі')
elif diagonal / 2 == r:
    print('Квадрат вписаний в коло')
else:
    print('Квадрат не поміститься в колі')
