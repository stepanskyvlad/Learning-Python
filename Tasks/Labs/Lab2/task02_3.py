"""
1.Ввести з клавіатури ціле число N (> 0).
2. Знайти добуток 1*2*…*N.
3. Для того, щоб уникнути переповнення, обчислювати цей добуток
за допомогою дійсної змінної
4. Вивести результат, як дійсне число.
"""


def get_number():
    while True:
        try:
            n = int(input("Enter an integer greater then zero: "))
            if not n > 0:
                continue
            elif n > 999:
                print("There will be RecursionError.\n"
                      "Enter the number less than 997")
                continue
        except ValueError as ve:
            print(f"There's an error: {ve}")
        else:
            break
    return n


# result = 1*2*…*N
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def main():
    n = get_number()
    result = factorial(n)
    print(f"Result is {result}")


if __name__ == "__main__":
    main()
