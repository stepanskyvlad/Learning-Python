import threading
import time


def long_square(num, result):
    time.sleep(1)
    result[num] = num**2


results = {}
t1 = threading.Thread(target=long_square, args=(1, results))
t2 = threading.Thread(target=long_square, args=(2, results))

t1.start()
t2.start()

t1.join()
t2.join()
print(results)
