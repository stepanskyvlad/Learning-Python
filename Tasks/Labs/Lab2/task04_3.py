"""
1.Ввести з клавіатури дійсне число A і ціле число N (> 0).
2.Знайти всі степені числа A, які не більше від числа N.
3.Вивести значення степенів та відповідні цілі показники степеня
числа А.
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


def solve_task(a, n):
    result = 1
    for i in range(1, n+1):
        result *= a
        if result < n:
            print(f"{a} raised to the {i}th power is equal {result}")


def main():
    a, n = get_numbers()
    solve_task(a, n)


if __name__ == "__main__":
    main()
