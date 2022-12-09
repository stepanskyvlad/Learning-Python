# Fibonacci's FizzBuzz
def fibs_fizz_buzz(n):
    a, b = 0, 1
    fib_list = []
    for _ in range(n):
        a, b = b, a + b
        if a % 3 == 0 and a % 5 == 0:
            fib_list.append('FizzBuzz')
        elif a % 3 == 0:
            fib_list.append('Fizz')
        elif a % 5 == 0:
            fib_list.append('Buzz')
        else:
            fib_list.append(a)
    return fib_list


print(fibs_fizz_buzz(20))
