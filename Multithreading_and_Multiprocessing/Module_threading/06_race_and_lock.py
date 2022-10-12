import concurrent.futures
import threading
import time


class BankAccount:
    def __init__(self):
        self.balance = 100  # shared data/resource
        self.lock_obj = threading.Lock()

    def update(self, transaction, amount):
        print(f"{transaction} started")

        # the next thread will manipulate with data, when the previous one finishes its work
        with self.lock_obj:
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(1)
            self.balance = tmp_amount

        # or
        # self.lock_obj.acquire()
        # tmp_amount = self.balance
        # tmp_amount += amount
        # time.sleep(1)
        # self.balance = tmp_amount
        # self.lock_obj.release()

        print(f"{transaction} ended")


if __name__ == "__main__":
    # create a locked object
    # lock_obj = threading.Lock()
    #
    # # return True, if an object is captured, else - False
    # print(lock_obj.locked())  # Now the object is not captured. Return False
    #
    # # to capture
    # lock_obj.acquire()
    # print(lock_obj.locked())  # return True
    #
    # # to release
    # lock_obj.release()
    # print(lock_obj.locked())  # return False

    acc = BankAccount()
    print(f"Main started. acc.balance={acc.balance}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.map(acc.update, ('refill', 'withdraw'), (100, -200))

    print(f"End of main. Balance={acc.balance}")
