def calculate_gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return calculate_gcd(num2, (num1 % num2))


number1 = int(input('Enter the first positive integer value: '))
number2 = int(input('Enter the second positive integer value: '))

print('The greatest common divisor of %d and %d is %d.' % (number1, number2, calculate_gcd(number1, number2)))
