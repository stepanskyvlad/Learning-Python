"""Випадковим чином створити список, що складається з елементів
цілого типу. Отримати новий список, який складається з цифр, що
знаходяться в молодших розрядах елементів початкового списку.
Сформувати з нього список з випадковими елементами, вдвічі
довший за початковий."""
import random


def create_list(max_number, number):
    """Випадковим чином створити список"""
    my_list = random.sample(range(max_number+1), number)
    return my_list


def change_list(list1):
    """Отримати новий список, який складається з цифр молодшого розряду"""
    new_list = [i % 10**(len(str(i)) - 1) for i in list1]
    return new_list


def create_long_list(list2):
    """Створити вдвічі довший список випадковим чином з отриманого списку"""
    long_list = random.choices(list2, k=len(list2)*2)
    return long_list


def main():
    my_list = create_list(x, y)
    new_list = change_list(my_list)
    long_list = create_long_list(new_list)
    print(f"Your list has been created:\n{my_list}\nThe list has been changed\n"
          f"{new_list}\nThe long list has been created\n{long_list}")


if "__main__" == __name__:
    x = int(input('Enter the max number in the range --> '))
    y = int(input("Enter the number of integers in the lists --> "))
    main()
