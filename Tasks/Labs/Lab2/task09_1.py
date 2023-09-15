import math


# solve this function without any errors
def calculate_func(x, y):
    result = ((2*x+y)**3) / (math.log(y+0.75))
    return result


def get_numbers():
    while True:
        try:
            x = float(input("Enter number x: "))
            y = float(input("Enter number y: "))
        except ValueError as ve:
            print(f"There's an error: {ve}")
        else:
            break
    return x, y


def calculate_safely(func):
    def safe_version(x, y):
        if y+0.75 < 0:
            print("There's a negative number in the logarithm")
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
