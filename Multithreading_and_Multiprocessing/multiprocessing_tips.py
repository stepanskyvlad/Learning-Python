from multiprocess import Process
import time


def long_square(num):
    time.sleep(1)
    # result[num] = num**2               <-- there aren't any results. Remember processes don't share memory. They get
    # a copy of this dictionary in their own separate memory space, and we have no way of accessing it, except if they
    # record it somewhere like a file system or a database.
    print(num ** 2)
    print("Finish computing!")


if __name__ == '__main__':
    # results = {} <-- there aren't any results.
    p1 = Process(target=long_square, args=(1, ))
    p2 = Process(target=long_square, args=(2, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    # print(results) <-- there aren't any results.
