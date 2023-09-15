import random

text = str()
with open(r"C:/lab7/Pavlush/20.txt", "r") as file:
    innerText = file.read()
    i = 0
    for line in innerText.split("\n"):
        if i == 0 or i == 3:
            text += line.strip() + ". "
        elif len(line) > 0:
            text += line.strip() + " "
        i += 1
sentences = list()

lastIndex = 0
for i in range(0, len(text)):
    symbol = text[i]
    if symbol == '.' or symbol == '?' or symbol == '!':
        result = None
        if symbol == '.' and i + 2 != len(text) and text[i + 1] == text[i + 2] == symbol:
            result = text[lastIndex:(i + 3)].strip()
            lastIndex = i + 3
        elif symbol == '?' and i + 1 != len(text) and text[i + 1] == '!':
            result = text[lastIndex:(i + 2)].strip()
            lastIndex = i + 2
        else:
            result = text[lastIndex:(i + 1)].strip()
            lastIndex = i + 1
        if len(result) > 1:
            sentences.append(result)

firstOut = str()

average_length = 0
for line in sentences:
    cur_length = 0
    for symbol in line:
        if symbol.isalpha():
            cur_length += 1
    average_length = (average_length + cur_length) / 2

sentencesCopy = sentences.copy()
random.shuffle(sentencesCopy)
for line in sentencesCopy:
    cur_length = 0
    for symbol in line:
        if symbol.isalpha():
            cur_length += 1
    if cur_length < average_length:
        formatted = line[0].upper() + line[1:]
        firstOut += formatted + "\n"

secondOut = str()
vowels = ["а", "о", "у", "и", "і", "е", "я", "ю", "є", "ї"]
capital_vowels = ["А", "О", "У", "И", "І", "Е", "Я", "Ю", "Є", "Ї"]
for symbol in innerText:
    if symbol in vowels or symbol in capital_vowels:
        if symbol.isupper():
            symbol = random.choice(capital_vowels)
        else:
            symbol = random.choice(vowels)
    secondOut += symbol

with open("C:/lab7/Pavlush/201.txt", "w+", encoding="utf-8") as file:
    file.write(firstOut)
with open("C:/lab7/Pavlush/202.txt", "w+", encoding="utf-8") as file:
    file.write(secondOut)
