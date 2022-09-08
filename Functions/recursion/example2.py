"""
The task:
1) Enter from keyboard a real number X and an integer N (>0)
2) Solve the function: B = x - x^3/3 + x^5/5 + ... +(-1)^N * (x^(2N+1))/(2N+1)
"""


def get_numbers():
    while True:
        try:
            x = float(input("Enter a real number: "))
            n = int(input("Enter an integer greater than zero: "))
            if not n > 0:
                continue
        except ValueError as ve:
            print(f"There's a problem - {ve}")
        else:
            break
    return x, n


# solving this function using recursion
def solve_func(x, n):
    if n == 0:
        return x
    return (-1)**n * (x**(2*n + 1))/(2*n + 1) + solve_func(x, n-1)


def main():
    x, n = get_numbers()
    result = solve_func(x, n)
    print(f"The result is {result}")


if __name__ == "__main__":
    main()
