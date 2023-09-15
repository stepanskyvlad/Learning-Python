"""
1.Ввести з клавіатури натуральне число N>100.
2.Сформувати послідовність від 10 до N.
3.Вивести на друк числа, яким відповідають натуральні числа, як
квадратні корені та самі ці квадратні корені (наприклад: 36 та 6).
4.Вивести на друк числа, яким відповідають натуральні числа, як
кубічні корені та самі ці кубічні корені (наприклад: 27 та 3).
"""


def get_number():
    number = 0
    try:
        while 0 >= number < 100:
            number = int(input('Enter a natural number greater than 100: '))
    except ValueError as ve:
        print(f"There's an error - {ve}")
    return number


# let's form a sequence from 10 tо N
def form_sequence(number):
    numbers = [n for n in range(10, number + 1)]
    return numbers


# Print natural numbers: n-th root of a number x
def print_roots_numbers(numbers):
    def root_degree(n):
        for x in numbers:
            if x % round(x ** (1 / n), 3) == 0:
                root = round(x ** (1 / n), 3)
                print(f"{root} - a root of degree {n} of number {x}")
            else:
                continue
    return root_degree


def main():
    number_list = form_sequence(get_number())
    choose_degree = print_roots_numbers(number_list)
    choose_degree(2)
    choose_degree(3)


if __name__ == "__main__":
    main()
