# Count the divisors of a number
def divisors(n):
    deno_list = []
    for denominator in range(1, n+1):
        if (n / denominator).is_integer():
            deno_list.append(denominator)
    return len(deno_list)


# other solutions
def divisors_1(n):
    divs = 0

    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            divs += 2

    return divs - (x * x == n)


def divisors_2(n):
    b = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            b.add(i)
            b.add(int(n / i))
    return b


print(divisors_1(30))

