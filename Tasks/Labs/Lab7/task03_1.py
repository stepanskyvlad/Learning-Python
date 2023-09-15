import os
import pickle
import shelve
import shutil

os.chdir(r"C://")

# Task1
try:
    os.mkdir("C://lab7")
    print("The directory's been created")
except FileExistsError:
    print("The directory already exists")

# Task2
try:
    os.mkdir("C://lab7//Shunevych")
    print("The subdirectory has been created")
except FileExistsError:
    print("The subdirectory already exists")

# Task3
try:
    shutil.copyfile(r"C:/3.txt", r"C:/lab7/Shunevych/3.txt")
    print("The file's downloaded in the subdirectory")
except FileExistsError:
    print("The file hasn't downloaded")

# Task4
try:
    os.mkdir("C://lab5")
    print("The directory's been created")
except FileExistsError:
    print("The directory already exists")
number_sunny_days = {
     "January": 11,
     "February": 10,
     "March": 12,
     "April": 16,
     "May": 18,
     "June": 21,
     "July": 25,
     "August": 22,
     "September": 19,
     "October": 17,
     "November": 13,
            }
with open('C://lab5//lab5_1.txt', 'wb') as file:
    pickle.dump(number_sunny_days, file)
with open('C://lab5//lab5_1.txt', 'rb') as file:
    information = pickle.load(file)
    information["December"] = 12
    for key in information:
        print("{:^2} : {} ".format(key, information[key]))
with open('C://lab5//lab5_2.txt', 'wb') as file:
    pickle.dump(information, file)

# Task5
try:
    os.mkdir("C://lab6")
    print("The directory's been created")
except FileExistsError:
    print("The directory already exists")
with shelve.open('C://lab6//lab6_1.txt', 'c') as file:
    file['January'] = 11
    file['February'] = 10
    file['March'] = 12
    file['April'] = 16
    file['May'] = 18
    file['June'] = 21
    file['July'] = 25
    file['August'] = 22
    file['September'] = 19
    file['October'] = 17
    file['November'] = 13
with shelve.open('C://lab6//lab6_1.txt', 'c') as file:
    file.pop('January')
    file.update({"December": 12})
    file.popitem()
    for i in file:
        print("{:^2} : {} ".format(i, file[i]))
