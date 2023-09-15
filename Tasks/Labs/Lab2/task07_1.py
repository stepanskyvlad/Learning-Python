import math


# solve this function without any errors
def calculate_func(x, y):
    result = (x**2+2.8*x+0.355) / (math.cos(2*y)+3.6)
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
        if (math.cos(2*y)+3.6) == 0:
            print("There's a division by zero")
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
