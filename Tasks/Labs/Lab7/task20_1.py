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
    os.mkdir("C://lab7//Pavlush")
    print("The subdirectory has been created")
except FileExistsError:
    print("The subdirectory already exists")

# Task3
try:
    shutil.copyfile(r"C:/20.txt", r"C:/lab7/Pavlush/20.txt")
    print("The file's downloaded in the subdirectory")
except FileExistsError:
    print("The file hasn't downloaded")

# Task4
try:
    os.mkdir("C://lab5")
    print("The directory's been created")
except FileExistsError:
    print("The directory already exists")
wikipedia = {
     "Історія":
         {"Археологія": (" М. Брайчевський", " О. Коцієвський"),
          "Нумізматика": (" Д. Фрейзер", " А. Бастіан"), },
     "Політика":
         {"Політична психологія": ("О. Майборода", "Филиппов А.В."),
          "Політична соціологія": ("Бацевич Ф. С.", "Є.Захаров"), },
     "Економіка":
         {"Мікроекономіка": ("М. Фрідман", "А. Філіппенко"),
          "Макроекономіка": ("Д. Любченко", "М. Фрідман"), },
     "Традиції":
         {"Українські": ("М. Левитський", "Ю. Юзич"),
          "Військові": ("В. Куін", "Г. Шумським"), },
     "Кінематографія":
         {"Каскадери": ("Ю. Бріннер", "Д. Дар"),
          "Кінооператори": ("Е. Лесні", "Луї Ле Пренс"), },
     "Персоналії":
         {"Зниклі": ("У. Абель", "Г. Лінгнер"),
          "Довгожителі": ("Г. Бейнс", "Х. Тійоно"), },
     "Література":
         {"Поети": ("Л. Костенко", "О. Олесь"),
          "Анти-утопія": ("Дж. Орвел", "Дж. Байрон"), },
     "Міста":
         {"Мегаполіси": ("Й. Матонго", "Д. Кроун"), },
     "Міфологія":
         {"Первісна": ("К. Рад", "М. Сіліліус"),
          "Сучасна": ("Клод Леві-Строс", "Б. Лобовик"), }, }
with open('C://lab5//lab5_1.txt', 'wb') as file:
    pickle.dump(wikipedia, file)
with open('C://lab5//lab5_1.txt', 'rb') as file:
    information = pickle.load(file)
    information["Мова"] = {"Синхронія": ("Фердинанд де Сосюр", "Бодуен де Куртене"),
                            "Діахронія": ("Ян Бодуен де Куртене", "В. І. Даль"), }
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
    file['Історія'] = "(Археологія, Нумізматика)"
    file['Політика'] = "(Політична психологія, Американські президенти)"
    file['Україна'] = "(Політика, Традиції)"
    file['Культура і мистецтво'] = "(Видатні митці, Культурна спадщина)"
    file['Література'] = "(Поезія, Анти-утопія)"
with shelve.open('C://lab6//lab6_1.txt', 'c') as file:
    file.pop('Політика')
    file.update({"Мова": "(Калька, Русифікація)"})
    file.popitem()
    for i in file:
        print("{:^2} : {} ".format(i, file[i]))
