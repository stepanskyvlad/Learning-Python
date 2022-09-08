"""
The task:
1) Enter from keyboard a real number A and an integer N (>0)
2) Solve the function: B = 1 + A + A^2 + A^3 + ... + A^N
3) Solve the function: C = 1 - A + A^2 - A^3 + A^4 - A^5 + ... (-1)^N*A^N
"""


def get_numbers():
    while True:
        try:
            a = float(input("Enter a real number: "))
            n = int(input("Enter an integer greater than zero: "))
            if not n > 0:
                print("The inger is not greater than zero!")
        except ValueError as ve:
            print(f"There's an error - {ve}")
        else:
            break
    return a, n


# B = 1 + A + A^2 + A^3 + ... + A^N
def solve_func1(a, n):
    if n == 0:
        return 1
    else:
        return a**n + solve_func1(a, n-1)


# C = 1 - A + A^2 - A^3 + A^4 - A^5 + ... (-1)^N*A^N
def solve_func2(a, n):
    if n == 0:
        return 1
    else:
        return (-1)**n * a**n + solve_func2(a, n-1)


def main():
    a, n = get_numbers()
    result1 = solve_func1(a, n)
    result2 = solve_func2(a, n)
    print(f"The final result of the first function is {result1}\n"
          f"The final result of the second function is {result2}\n")


if __name__ == "__main__":
    main()
