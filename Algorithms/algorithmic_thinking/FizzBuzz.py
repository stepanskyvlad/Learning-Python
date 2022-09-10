numbers = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        numbers.append("FizzBuzz")
    elif i % 3 == 0:
        numbers.append("Fizz")
    elif i % 5 == 0:
        numbers.append('Buzz')
    else:
        numbers.append(i)
print(numbers)
