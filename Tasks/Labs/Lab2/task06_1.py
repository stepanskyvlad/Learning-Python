import math


# solve this function without any errors
def calculate_func(x, y):
    result = (0.81*math.cos(x)) / (math.log(y)+2*x**3)
    return result


def get_numbers():
    while True:
        try:
            x = float(input('Enter the number x: '))
            y = float(input('Enter the number y: '))
        except ValueError as ve:
            print(f'There\'s {ve}.\nPlease, enter numbers')
        else:
            break
    return x, y


def calculate_safely(func):
    def safe_version(x, y):
        if y < 0:
            print("There's a negative number in the logarithm."
                  "\nEnter a positive number 'y'")
            return
        elif math.log(y)+2*x**3 == 0:
            print("Denominator is equal zero. \nEnter other numbers")
            return
        return func(x, y)

    return safe_version


def main():
    safe_calculation = calculate_safely(calculate_func)
    x, y = get_numbers()
    result = safe_calculation(x, y)
    if result is not None:
        print(f"There's result - {result:.3f}")


if __name__ == "__main__":
    main()
