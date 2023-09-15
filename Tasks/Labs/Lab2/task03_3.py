"""
1.Ввести з клавіатури дійсне число A і ціле число N (> 0).
2. Знайти A в степені N шляхом множення числа А самого на себе
A^N = A · A ·…· A (числа A перемножуються N разів).
3. Вивести проміжні результати множення та кінцевий результат
"""


def get_numbers():
    while True:
        try:
            a = float(input("Enter a real number: "))
            n = int(input("Enter an integer greater than zero: "))
            if not n > 0:
                print("The inger is not greater than zero!")
        except ValueError as ve:
            print(f"There's an error - {ve}")
        else:
            break
    return a, n


def power_of_number(a, n):
    result = 1
    for i in range(n):
        result *= a
        print(f"Now the result is {result}")
    return result


def main():
    a, n = get_numbers()
    result = power_of_number(a, n)
    print(f"The final result is {result}")


if __name__ == "__main__":
    main()
