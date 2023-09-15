import math


# solve this function without any errors
def calculate_func(x, y, z, a, b):
    result = (math.sqrt(x + 2.6 * y * math.sin(z))) / (a - b ** 3)
    return result


def get_numbers():
    while True:
        try:
            x = float(input("Enter X: "))
            y = float(input("Enter Y: "))
            z = float(input("Enter Z: "))
            a = float(input("Enter A: "))
            b = float(input("Enter B: "))
        except ValueError as ve:
            print(f"There's an error: {ve}")
        else:
            break
    return x, y, z, a, b


def calculate_safely(func):
    def safe_version(x, y, z, a, b):
        if not -1 <= z <= 1:
            print("There's a wrong number in the sin.")
            return
        elif x + 2.6 * y * math.sin(z) < 0:
            print("There's negative number in the square root")
            return
        elif (a - b ** 3) == 0:
            print('There\'s a division by zero')
            return
        return func(x, y, z, a, b)

    return safe_version


def main():
    safe_calculation = calculate_safely(calculate_func)
    x, y, z, a, b = get_numbers()
    result = safe_calculation(x, y, z, a, b)
    if result is not None:
        print(f"There's result - {result:.3f}")


if __name__ == "__main__":
    main()
