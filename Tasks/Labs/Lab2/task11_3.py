# solve: B = 1 + X + (X^2)/2 + ... + (x^n)/n

def get_number():
    while True:
        try:
            x = float(input("Enter a real number: "))
            n = float(input("Enter a natural number: "))
            if n <= 0:
                print(f"{n} is not a natural number. Try again!")
        except ValueError as ve:
            print(f"There is an error - {ve}")
        else:
            break


def solve_func(x, n):
    pass

