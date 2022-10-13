import random
import threading
import time
import datetime


class HorseRace:
    def __init__(self):
        self.barrier = threading.Barrier(4)  # кількість потоків, які досягають бар'єру і чекають
        self.horses = ['Artax', 'Frankel', 'Bucephalus', 'Barton']

    def lead(self):
        horse = self.horses.pop()
        time.sleep(random.randrange(1, 5))
        print(f"\n{horse} reached the barrier at: {datetime.datetime.now()}")
        # Спочатку всі потоки підходять до бар'єра і тільки тоді починається виконання
        # поки wait() не було викликано 4 рази, всі потоки чекали.
        # Як тільки всі потоки були готові до виконання, бар'єр їх відпустив
        self.barrier.wait()

        # емуляція виконання роботи
        time.sleep(random.randrange(1, 5))
        print(f"\n{horse} started at: {datetime.datetime.now()}")

        time.sleep(random.randrange(1, 5))
        print(f"\n{horse} finished at: {datetime.datetime.now()}")

        self.barrier.wait()  # поки всі потоки не завершили роботу,
        # наступний рядок коду не був доступним на виконання
        print(f"\n{horse} went sleeping")


if __name__ == "__main__":
    print(f"Race preparation")

    race = HorseRace()
    for x in range(4):
        thread = threading.Thread(target=race.lead)
        thread.start()
