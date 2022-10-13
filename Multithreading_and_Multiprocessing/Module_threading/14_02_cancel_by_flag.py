import threading
import time

from Multithreading_and_Multiprocessing.Module_threading.count_three_sum import read_ints

should_stop = False  # add the flag, which helps to terminate a thread


def count_three_sum(ints, thread_name="t"):
    print(f'started count_three_sum in {thread_name}')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # замість того, щоб грубо завершувати процес за допомогою terminate()
                # після if можна записати різні інструкції на виконання перед завершенням процесу
                # Наприклад: закрити файл, почистити ресурс і повернули якусь інфу
                if should_stop:  # using flag to terminate
                    print("Task was Cancelled")
                    counter = -1
                    return counter

                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f"Triple found int {thread_name}: {ints[i]}, {ints[j]}, {ints[k]}", end='\n')

    print(f"Ended count_three_sum in {thread_name}. Triplets counter={counter}")
    return counter


if __name__ == "__main__":
    print('started main')

    ints = read_ints("data\\1Kints.txt")

    # створюємо потік
    t = threading.Thread(target=count_three_sum, args=(ints,))
    t.start()  # початок виконання

    time.sleep(5)  # даємо виконуватися потоку 5 секунд

    should_stop = True  # завершуємо процес за допомогою створеного Flag

    time.sleep(2)

    print('ended main')
