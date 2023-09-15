line = bytearray(input("Введіть послідовність символів: "), "cp1251")
word = bytearray(input("Введіть окреме слово: "), "cp1251")
if word.isalpha():
    print(line.count(word))
else:
    print("Вам потрібно ввести слово")
