# Kata name: Fibonacci - Create function fib that returns n'th element of Fibonacci sequence

# Class (iteration)
class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


# recursion
def fibonacci_r(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    if n in {0, 1}:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


# recursion with memoization
cache = {0: 0, 1: 1}


def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]


print([fibonacci_of(n) for n in range(11)])


# my solution
def fibonacci(n: int) -> int:
    n1, n2 = 0, 1
    counter = 0
    while counter < n:
        nth = n1 + n2
        n1, n2 = n2, nth
        counter += 1
    return n1


# other solutions
def fibonacci_1(n: int) -> int:
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fibonacci_of3(n):
    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    # Handle the base cases
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


print(fibonacci(10))
print(fibonacci_of(10))
fibonacci_of2 = Fibonacci()
print(fibonacci_of2(10))
print(fibonacci_of3(10))
