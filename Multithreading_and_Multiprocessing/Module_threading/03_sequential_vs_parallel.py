import threading

from Multithreading_and_Multiprocessing.Module_threading.count_three_sum import read_ints, count_three_sum
from Multithreading_and_Multiprocessing.Module_threading.decorators import measure_time


@measure_time
def run_in_parallel(ints):
    t1 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't1'))
    t2 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't2'))

    t1.start()
    t2.start()

    print('\nGoing to wait for threads\n')

    t1.join()
    t2.join()


@measure_time
def run_sequentially(ints):
    count_three_sum(ints, 'main1')
    count_three_sum(ints, 'main2')


if __name__ == "__main__":
    print('started main')
    ints = read_ints('../data\\1Kints.txt')

    run_in_parallel(ints)
    run_sequentially(ints)

    print('ended main')
