import math


def calculate_safely(func):
    def wrapper(x, y):
        if math.sin(x) == 0:
            print('There\'s zero in denominator!\nTry again!')
            return None
        return func(x, y)

    return wrapper


@calculate_safely
def solve_function(x: float, y: float):
    result = math.pow(x, 2) + ((0.5*y + 4.8) / (math.sin(x)))
    return result


def get_numbers():
    while True:
        try:
            x = float(input("Enter number X: "))
            y = float(input("Enter number Y: "))
        except ValueError as ve:
            print(f"There's an error - {ve}\nTry again!")
        else:
            break
    return x, y


def main():
    x, y = get_numbers()
    result = solve_function(x, y)
    if result is not None:
        print(f"There's result --> {result:.3f}")


if __name__ == "__main__":
    main()
