import multiprocessing
import time

from Multithreading_and_Multiprocessing.Module_threading.count_three_sum import read_ints, count_three_sum

if __name__ == "__main__":
    print('started main')

    ints = read_ints("data\\1Kints.txt")

    # створюємо процес
    p = multiprocessing.Process(target=count_three_sum, args=(ints,))
    p.start()  # початок виконання

    time.sleep(5)  # даємо виконуватися процесу 5 секунд

    p.terminate()  # завершуємо процес, а з ним же і потік

    print('ended main')
