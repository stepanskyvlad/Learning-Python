"""
Задайте словник результатів тестування, вказуючи як ключ прізвище
учасника, а як значення – кількість балів. Кількість балів згенерувати
випадковим чином. Максимальна кількість балів – 100. Визначити
трьох переможців та передбачити відповідь на запитання про
наявність людини серед учасників.
"""
import random


test_dict = {}
sur_list = []
while True:
    surname = str(input(f"If you want to stop press 'Q'."
                        f"\nEnter a student's surname: "))
    if surname == 'q' or surname == 'Q':
        print('Stopping the process...')
        break
    else:
        sur_list.append(surname)

score_list = random.choices(range(101), k=len(sur_list))
print(sur_list)
print(score_list)
for k, v in zip(sur_list, score_list):
    test_dict[k] = v

print(test_dict)
new_dict = dict(sorted(test_dict.items(), key=lambda item: item[1], reverse=True))
print(new_dict)
for k, v in list(new_dict.items())[:3]:
    print(f"Winners:\n{k} - {v} points")

check = str(input("Is this person on the list? :"))
if check in test_dict:
    print(f'{check} is on the list')
else:
    print(f'{check} isn\'t on the list')
