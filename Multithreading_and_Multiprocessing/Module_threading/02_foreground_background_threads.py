import threading
import time

from Multithreading_and_Multiprocessing.Module_threading.count_three_sum import read_ints, count_three_sum

if __name__ == "__main__":
    print('started main')

    ints = read_ints('../data\\1Kints.txt')

    # we can use args: args=(ints,) or kwargs=dict(ints=ints)
    t1 = threading.Thread(target=count_three_sum, kwargs=dict(ints=ints), daemon=True)
    t1.start()  # start of thread execution

    print(input('What is your name?: '))

    t1.join()  # the thread must end before main ends
    print('Ended main')
