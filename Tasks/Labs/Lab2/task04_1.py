import math


# solve this function without any errors
def calculate(x, y):
    result = (9.33*x**3+math.sqrt(x)) / (math.log(y+3.5)+math.sqrt(y))
    return result


def get_numbers():
    while True:
        try:
            x = float(input("Enter number x: "))
            y = float(input("Enter number y: "))
        except ValueError as ve:
            print(f"There is an error: {ve}\nPlease, try again!")
        else:
            break
    return x, y


def calculate_without_errors(func):
    def safe_version(x, y):
        if x < 0 or y < 0:
            print('A square root of number error.'
                  '\nPlease, enter "x" and "y" greater than zero!')
            return
        elif y+3.5 < 0:
            print("There's the number less than zero in the logarithm")
            return
        elif math.log(y+3.5)+math.sqrt(y) == 0:
            print("The denominator is equal zero")
            return
        return func(x, y)

    return safe_version


def main():
    secure_computing = calculate_without_errors(calculate)
    x, y = get_numbers()
    result = secure_computing(x, y)
    if result is not None:
        print('Result is {:.3f}'.format(result))


if __name__ == "__main__":
    main()
