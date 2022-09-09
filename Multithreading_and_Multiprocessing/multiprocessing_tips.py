from multiprocessing import Process
import time


def long_square(num, result):
    time.sleep(1)
    result[num] = num**2


results = {}
p1 = Process(target=long_square, args=(1, results))
p2 = Process(target=long_square, args=(2, results))

p1.start()
p2.start()

p1.join()
p2.join()
print(results)
