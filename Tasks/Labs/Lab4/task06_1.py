"""
Розрахувати значення елементів списку Y за формулою
y = math.pow(i, 2) - 2*i + 19.3*math.cos(i). Сформувати новий список, розмістивши в ньому
спочатку елементи, значення яких менші за середнє арифметичне, а
потім – ті значення, що дорівнюють або більші за середнє
арифметичне елементів початкового списку. Вивести обидва списки.
"""
import random
import math


def formula(i):
    result = math.pow(i, 2) - 2*i + 19.3*math.cos(i)
    return result


def get_new_list(my_list, av_num):
    new_list = [i for i in my_list if i < av_num]
    for j in my_list:
        if j >= av_num:
            new_list.append(j)
    return new_list


def get_random_list(max_n, n):
    random_list = random.sample(range(max_n + 1), n)
    return random_list


def main():
    max_number = int(input("Enter the max number in the range --> "))
    number = int(input("Enter the number of the list --> "))
    y = get_random_list(max_number, number)
    result_list = [round(formula(i), 2) for i in y]
    average_num = round(sum(result_list) / len(result_list), 2)
    second_list = get_new_list(result_list, average_num)
    print(f'List Y:\n{y}\nResult list:\n{result_list}\nAverage number -> {average_num}'
          f'\nNew list:\n{second_list}')


if "__main__" == __name__:
    main()