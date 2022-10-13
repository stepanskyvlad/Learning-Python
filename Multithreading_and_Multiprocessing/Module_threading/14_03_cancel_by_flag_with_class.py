import threading
import time

from Multithreading_and_Multiprocessing.Module_threading.count_three_sum import read_ints


class ThreeSumTask:

    def __init__(self, ints):
        self.ints = ints
        self.canceled = False  # create a flag
        self.lock_obj = threading.Lock()  # create a lock

    def run(self):
        self.count_three_sum(self.ints)

    def cancel(self):  # func which terminate threads
        with self.lock_obj:
            self.canceled = True

    def count_three_sum(self, ints):
        print(f'started count_three_sum')

        n = len(ints)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.canceled:  # using flag to terminate
                        print("Task was Cancelled")
                        counter = -1
                        return counter

                    if ints[i] + ints[j] + ints[k] == 0:
                        counter += 1
                        print(f"Triple found: {ints[i]}, {ints[j]}, {ints[k]}", end='\n')

        print(f"Ended count_three_sum. Triplets counter={counter}")
        return counter


if __name__ == "__main__":
    print('started main')

    ints = read_ints("../data\\1Kints.txt")

    # створюємо потік
    task = ThreeSumTask(ints)
    t = threading.Thread(target=task.run)
    t.start()  # початок виконання

    time.sleep(5)  # даємо виконуватися потоку 5 секунд

    task.cancel()  # terminate the thread

    t.join()

    print('ended main')
