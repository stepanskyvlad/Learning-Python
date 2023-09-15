import math


# solve this function without any errors
def calculate_func(x, y):
    result = math.log(x) + ((3.5 * x + 1) / (math.cos(2 * y)))
    return result


def get_numbers():
    while True:
        try:
            x = float(input("Enter number 'x': "))
            y = float(input("Enter number 'y': "))
        except ValueError as ve:
            print(f"There is {ve}. \nPlease, enter your numbers again!")
        else:
            break
    return x, y


def calculate_safely(func):
    def safe_version(x, y):
        if x < 0:
            print("There's number less than zero in the logarithm.")
            return
        elif math.cos(2 * y) == 0:
            print("The denominator is equal zero")
            return
        return func(x, y)

    return safe_version


def main():
    safe_calculation = calculate_safely(calculate_func)
    x, y = get_numbers()
    result = safe_calculation(x, y)
    if result is not None:
        print(f"Result is {result:.3f}")


if __name__ == '__main__':
    main()
