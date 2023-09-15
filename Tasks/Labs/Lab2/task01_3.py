"""
1.Ввести з клавіатури два цілих числа A і B (A <B).
2.Знайти всі цілі числа, що розташовані між даними числами
(включаючи самі ці числа),
3. Вивести числа в порядку їх зростання.
4.Вивести кількість N цих чисел.
"""


def get_numbers():
    while True:
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            if not a < b:
                print("The first number is not less than the second one."
                      " \nPlease, try again")
                continue
        except ValueError as ve:
            print(f"There's an error - {ve}")
        else:
            break
    return a, b


def find_all_integers_btw(a, b):
    my_list = [i for i in range(a, b+1)]
    return my_list


def print_len_of_list(my_list):
    print(f"The amount of the numbers is {len(my_list)}")


def main():
    a, b = get_numbers()
    numbers_list = find_all_integers_btw(a, b)
    print(f"List of integers - {numbers_list}")
    print_len_of_list(numbers_list)


if __name__ == "__main__":
    main()
