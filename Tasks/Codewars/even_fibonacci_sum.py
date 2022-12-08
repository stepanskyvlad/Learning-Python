# Even Fibonacci Sum
def even_fib(m):
    cache = []
    a, b = 0, 1
    for i in range(0, m):
        a, b = b, a + b
        if a >= m:
            break
        elif a % 2 == 0:
            cache.append(a)
    return sum(cache)


# another solution
def even_fib_1(m):
    x, y = 0, 1
    counter = 0
    while y < m:
        if y % 2 == 0:
            counter += y
        x, y = y, x + y
    return counter


print(even_fib(8))
