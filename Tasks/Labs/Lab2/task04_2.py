import math

while True:
    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))
    c = float(input("Enter the length of side C: "))
    if a > b+c or b > a+c or c > a+b:
        print("The lengths are wrong. Try again!")
        continue
    else:
        if a == math.sqrt(b**2 + c**2):
            print(f"The legs are b={b} and c={c}. The hypotenuse is a={a}")
        elif b == math.sqrt(a**2 + c**2):
            print(f"The legs are a={a} and c={c}. The hypotenuse is b={b}")
        elif c == math.sqrt(a**2 + b**2):
            print(f"The legs are b={b} and a={a}. The hypotenuse is c={c}")
        elif a == b == c:
            print("Triangle is equilateral")
        elif a == b or b == c or c == a:
            print("Triangle is isosceles")
        else:
            print("Triangle is multifaceted")
        break
