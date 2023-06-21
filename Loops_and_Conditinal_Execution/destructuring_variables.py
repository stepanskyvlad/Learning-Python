people = [('John', 33, 'Lawyer'), ('Michael', 35, 'Writer'), ('Michael', 27, 'Chef'), ('Ava', 49, 'Writer')]

for name, _, profession in people:  # if we name variable like "_", it means we won't use this
    print(f"Name is {name}, profession is {profession}")

*head, tail = [1, 2, 3, 4, 5]
print(*head)  # 1 2 3 4
print(tail)  # 5
