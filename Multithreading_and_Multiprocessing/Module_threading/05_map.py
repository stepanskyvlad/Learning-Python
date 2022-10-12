import concurrent.futures

from Multithreading_and_Multiprocessing.Module_threading.count_three_sum import read_ints, count_three_sum

# we use map when we need to execute the same func a few times.
if __name__ == "__main__":
    print('started main')

    data = read_ints('data\\1Kints.txt')
    # max_workers - the specified number of threads that can work simultaneously
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        results = executor.map(count_three_sum, (data, data), ('t1', 't2'))
        print('After map')
        for r in results:
            print(f"{r=}")
        print('End of map')

    print('ended main')
