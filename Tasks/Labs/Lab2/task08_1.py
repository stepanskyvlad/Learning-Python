import math


# solve this function without any errors
def calculate_func(x, y):
    result = (2.37*math.sin(x+1)) / (math.sqrt(4*y**2-0.1*y+5))
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
        if 4*y**2-0.1*y+5 < 0:
            print("There's a negative number in the square root")
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
