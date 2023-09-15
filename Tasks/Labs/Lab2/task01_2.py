a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
sum1 = (a+b)**2
sum2 = (a**2 + b**2)
print(f"Square amounts: sum1 - {sum1}")
print(f"Amount of squares: sum2 - {sum2}")
if sum1 > sum2:
    print(f"Sum1({sum1}) is greater than sum2({sum2})")
elif sum1 < sum2:
    print(f"Sum2({sum2}) is greater than sum1({sum1})")
else:
    print(f'Sum1({sum1}) is equal to sum2({sum2})')
