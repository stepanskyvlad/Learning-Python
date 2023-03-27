# Count the divisors of a number
# https://www.codewars.com/kata/542c0f198e077084c0000c2e

def divisors(n):
    divs = 0
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            if n / i == i:
                divs += 1
            else:
                divs += 2

    return divs


if __name__ == "__main__":
    print(divisors(12))
