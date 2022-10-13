import threading
import time


class NightClub:
    def __init__(self):
        self.bouncer = threading.Semaphore(3)  # 3 - максимальна кількість потоків, яка виконується "одночасно"

    def open_club(self):
        for x in range(1, 51):  # 50 - кількість потоків в черзі на виконання
            t = threading.Thread(target=self.guest, args=[x])
            # потік ставиться в чергу на виконання,
            # але почне виконуватися лише після виклику функції acquire()
            t.start()

    def guest(self, guest_id):
        print(f'\nGuest {guest_id} is waiting to entering night club')
        self.bouncer.acquire()  # потік приймається на виконання

        print(f'\nGuest {guest_id} is doing some dancing')
        time.sleep(1)  # емуляція виконання якоїсь роботи

        print(f'\nGuest {guest_id} is leaving the night club')
        self.bouncer.release()  # потік відпускається


if __name__ == '__main__':
    club = NightClub()
    club.open_club()
