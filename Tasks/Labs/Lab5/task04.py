"""Задайте словник, вказуючи як ключ назву підручника, а як значення –
кількість сторінок, які задані випадковим чином. Знайти найдорожчий
підручник, якщо ціна друку однієї сторінки однакова у всіх підручниках
і складає 50 коп."""
import random

max_num = 1
while True:
    try:
        max_num = int(input("Enter a maximum number of pages: "))
    except ValueError as ve:
        print('You entered not a integer.')
        continue
    else:
        break

textbook_list = []
while True:
    textbook = str(input(f"Enter q to finish the proces:"
                         f"\nEnter a title of the book: "))
    if textbook == 'q' or textbook == 'Q':
        break
    else:
        textbook_list.append(textbook)

num_pages = random.sample(range(1, max_num+1), k=len(textbook_list))
print(textbook_list)
print(num_pages)

textbook_dict = {}
for k, v in zip(textbook_list, num_pages):
    textbook_dict[k] = v
print(textbook_dict)

exp_book = max(textbook_dict.items(), key=lambda items: items[1])
print(f"The most expansive book is \"{exp_book[0]}\" - {exp_book[1] * 0.5} hryvnas")
