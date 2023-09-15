"""
Задайте словник, вказуючи як ключ місяць року, а як значення –
кількість сонячних днів, які задані випадковим чином. Виведіть місяць,
який має середню кількість сонячних днів, місяць, що має найбільшу
кількість сонячних днів, та місяць з найменшою кількістю сонячних
днів.
"""
import random


def sunny_days(month_name):
    if month_name == 'February':
        num = random.choice(range(29))
    elif month_name == 'June' or month_name == 'April' or month_name == 'September' or month_name == 'November':
        num = random.choice(range(31))
    else:
        num = random.choice(range(32))
    return num


month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
month_dict = {}
for i in month_list:
    month_dict[i] = sunny_days(i)
print(month_dict)
max_days = max(month_dict.items(), key=lambda item: item[1])
min_days = min(month_dict.items(), key=lambda item: item[1])
print(f"Maximum number of sunny days:\n{max_days[0]} - {max_days[1]}\n"
      f"Minimum number of sunny days:\n{min_days[0]} - {min_days[1]}")

average_num = sum(month_dict.values())/len(month_dict)
print(f"{average_num} - average number of sunny days in month")
near_ave = max_days[1]
for k, v in month_dict.items():
    if abs(average_num - v) < near_ave:
        near_ave = abs(average_num-v)
        ave_month = (k, v)

print(f'{ave_month[0]} has average numbers of sunny days - {ave_month[1]}')
