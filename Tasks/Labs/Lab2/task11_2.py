# Ввести натуральне число N.
# 1. Визначити, чи є воно парним
# 2. Визначити, чи ділиться воно без остачі на 3.
# 3. Визначити чи ділиться воно без остачі на 5.
# 4. Вивести повідомлення по кожній з даних перевірок
# 5. Вивести числа, які потрібно додати до числа N, щоб отримати подільність на 3 та на 5.
def get_number():
    while True:
        try:
            number = int(input("Enter a natural number: "))
            if number <= 0:
                print('The number is equal zero or less.\nTry again!')
                continue
        except ValueError as ve:
            print(f"There's an error - {ve}\nTry again")
        else:
            break
    return number


def is_even(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


def is_divisible_by_3(number):
    if number % 3 == 0:
        print("The number is divisible by 3")
    else:
        print("The number is not divisible by 3")


def is_divisible_by_5(number):
    if number % 5 == 0:
        print("The number is divisible by 5")
    else:
        print("The number is not divisible by 5")


def should_add(number):
    print(f"To get divisibility by 3, you should add {0 if number%3==0 else 3 - number%3}\n"
          f"To get divisibility by 5, you should add {0 if number%5==0 else 5 - number%5}")


def main():
    number = get_number()
    for func in [is_even, is_divisible_by_3, is_divisible_by_5, should_add]:
        func(number)


if __name__ == "__main__":
    main()
