import math


x1, y1 = (float(input('Enter x1: ')), float(input("Enter y1: ")))
x2, y2 = (float(input("Enter x2: ")), float(input('Enter y2: ')))
x0, y0 = (0, 0)

OA = math.sqrt((x1-x0)**2 + (y1-y0)**2)
OB = math.sqrt((x2-x0**2) + (y2-y0)**2)
print(f"The distance of OA is {OA}. \nThe distance of OB is {OB}")
if OA > OB:
    print(f"Point A is more distant then point B")
elif OB > OA:
    print("Point B is more distant than point A")
else:
    print("The distances are the same")
