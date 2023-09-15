import math


# solve this function without any errors
def calculate_func(x, y, z):
    result = (7.8*x**2+3.52*y)/(math.log(x+2*z)+math.exp(z))
    return result


def get_numbers():
    while True:
        try:
            x = float(input('Enter number x: '))
            y = float(input('Enter number y: '))
            z = float(input('Enter number z: '))
        except ValueError as ve:
            print(f"There's an error: {ve} \nPlease, enter numbers")
        else:
            break
    return x, y, z


def calculate_safely(func):
    def safe_version(x, y, z):
        if (x+2*z) < 0:
            print("There's a number less than zero in the logarithm")
            return
        elif z > 709:
            print("There's OverflowError: math range error. Enter z less than 709")
            return
        elif math.log(x+2*z)+math.exp(z) == 0:
            print('The denominator is equal zero')
            return
        return func(x, y, z)

    return safe_version


def main():
    safe_calculation = calculate_safely(calculate_func)
    x, y, z = get_numbers()
    result = safe_calculation(x, y, z)
    if result is not None:
        print(f"There's result - {result:.3f}")


if __name__ == "__main__":
    main()
