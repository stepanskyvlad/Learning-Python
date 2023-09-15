"""Випадковим чином створити два списки дійсних чисел. Сформувати
третій список з упорядкованих за зростанням значень елементів обох
списків. Визначити, чи є серед елементів елемент зі значенням 0."""
import numpy


def user_input():
    max_number = 0
    number = 0
    while True:
        try:
            max_number = float(input("Enter the max number in the range --> "))
            number = int(input("Enter the number of the real numbers --> "))
        except ValueError as ve:
            print(f"There`s an error -- > {ve}")
            continue
        else:
            break
    return max_number, number


def create_lists(max_number, number):
    first_list = list(numpy.random.uniform(0, max_number, number))
    second_list = list(numpy.random.uniform(0, max_number, number))
    print(f"{first_list}\n{second_list}")
    return first_list, second_list


def sort_list(list1, list2):
    new_list = sorted((list1 + list2))
    print(new_list)
    return new_list


def find_zero(user_list):
    if 0 in user_list:
        print("There's zero in the list")
    else:
        print("There isn't zero in the list")


def main():
    max_number, number = user_input()
    first_list, second_list = create_lists(max_number, number)
    new_list = sort_list(first_list, second_list)
    find_zero(new_list)


if '__main__' == __name__:
    main()
