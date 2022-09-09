import threading
import time


def long_square(num, result):
    time.sleep(1)
    result[num] = num**2


results = {}
threads = [threading.Thread(target=long_square, args=(n, results)) for n in range(0, 100)]
[t.start() for t in threads]
[t.join() for t in threads]
print(f"{results}")
