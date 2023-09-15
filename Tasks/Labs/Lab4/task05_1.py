"""
Випадковим чином створити два списки X і Y, що складаються з
елементів цілого типу. Сформувати список S, що складається з
однакових елементів початкових списків. Визначити довжину
отриманого списку, вставити значення в кінець списку.
"""
import random


max_number = int(input("Enter the max number in the range --> "))
number = int(input("Enter the number of integers in the lists --> "))

x = random.sample(range(max_number+1), number)
y = random.sample(range(max_number+1), number)
print(f"{x}\n{y}")

s = list(set(x).intersection(set(y)))
print(s)
s.append(len(s))
print(s)
