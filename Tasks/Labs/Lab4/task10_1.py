import random
import math
from functools import wraps


# get list with random integers
def get_xlist():
    while True:
        try:
            min_num = int(input("Enter a minimum integer in the list: "))
            max_num = int(input("Enter a maximum integer in the list: "))
            amount = int(input("Enter a number of integers: "))
            if (min_num >= max_num) or (amount <= 1):
                print("You've entered the wrong number. Please, try again")
                continue
        except ValueError as ve:
            print(f"There's an error - {ve}")
        else:
            x_list = random.choices(range(min_num, max_num), k=amount)
            return x_list


# solve functions without crashing of the program
def safe_calculation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError as ve:
            print(f"There's the error - {ve}")
        except TypeError as te:
            print(f"There's the error - {te}")
        except KeyError as ke:
            print(f"There's the error - {ke}")
        except Exception as e:
            print(f'Unknown error: {e}')
        else:
            return func(*args, **kwargs)

    return wrapper


# solve functions: y = x^3 - 7.5 if cos(x) > 0 or
# y = x^2 - 5e^sin(x) if x <= 0
@safe_calculation
def solve_func(x_list):
    y_list = []
    for x in x_list:
        if math.cos(x) > 0:
            y = x**3 - 7.5
            y_list.append(round(y, 2))
        elif math.cos(x) <= 0:
            y = x**2 - 5*math.exp(math.sin(x))
            y_list.append(round(y, 2))
    return y_list


# sort two lists and create new one from them
def sort_lists(x_list, y_list):
    y_list.sort()
    x_list.sort(reverse=True)
    return x_list, y_list


def get_rlist(x_list, y_list):
    r_list = x_list[::2] + y_list[::2]
    return r_list


# get random number from R list and check if this number in Y list
def get_and_check(r_list, y_list):
    ran_num = random.choice(r_list)
    if ran_num in y_list:
        print(f"The number {ran_num} is in Y list")
    else:
        print(f"There isn't the number {ran_num} in Y list")


if __name__ == "__main__":
    my_xlist = get_xlist()
    my_ylist = solve_func(my_xlist)
    if my_ylist is not None:
        print(my_xlist, my_ylist)
        sort_lists(my_xlist, my_ylist)
        print(my_xlist, my_ylist)
        my_rlist = get_rlist(my_xlist, my_ylist)
        print(my_rlist)
        get_and_check(my_rlist, my_ylist)
