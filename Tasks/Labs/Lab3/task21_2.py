my_string = bytearray(input("Введіть рядок: "), "cp1251")
my_list = my_string.split()
best = 0
for index in range(len(my_list)):
    if len(my_list[index]) > len(my_list[best]):
        best = index
print(f"Найдовше слово: {my_list[best].decode(encoding='cp1251')}"
      f"\nДовжина слова: {len(my_list[best])}")
