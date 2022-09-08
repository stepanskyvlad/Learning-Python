# We have 200 tasks and 10 students. We have to divide these 200 tasks among these students randomly.
import random


task_list = list(range(1, 201))
for i in range(0, 10):
    student = random.sample(task_list, 20)
    for j in student:
        task_list.remove(j)
    with open('file1.txt', 'a+') as file:
        file.write(f"{student}\n")
    print(student)
