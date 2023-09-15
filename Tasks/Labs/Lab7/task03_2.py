import os
os.chdir("C://lab7//Shunevych")

f2 = open("3part1.txt", "w", encoding="cp1251")
f3 = open("3part2.txt", "w", encoding="cp1251")

with open("3.txt", "r") as f1:
    """Розбиття файлу v3.txt на 2 частини. Перша - парні символи. Друга - непарні символи."""
    text = f1.read()
    for i in range(len(text)):
        if i % 2 == 0:
            f2.write(text[i])
        elif i % 2 != 0:
            f3.write(text[i])

f2.close()
f3.close()

f2 = open("3part1.txt", "r", encoding="cp1251")
f3 = open("3part2.txt", "r", encoding="cp1251")
a2 = f2.read()
a3 = f3.read()

with open("new_v3.txt", "w", encoding="UTF-8") as new_v3:
    """Відновлення початкового файлу з двох створених"""
    for i in range(len(a3)):
        new_v3.write(a2[i])
        new_v3.write(a3[i])

f2.close()
f3.close()
