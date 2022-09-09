from multiprocess import Process
import time


def long_square(num):
    time.sleep(1)
    print(num ** 2)
    print('Finished computing!')


if __name__ == '__main__':
    processes = [Process(target=long_square, args=(n, )) for n in range(0, 10)]
    [p.start() for p in processes]
    [p.join() for p in processes]
