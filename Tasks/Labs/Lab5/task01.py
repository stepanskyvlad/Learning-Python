"""
Використовуючи словник, задайте меню, вказуючи як ключ назву
страви, а як значення – її ціну. Виведіть меню, відсортоване за ціною
страв та за назвами страв за алфавітом.
"""
menu = {
    "Salad": 99,
    "Soup": 49,
    "Pizza": 89,
    "Chicken": 149,
    "Ice cream": 29,
    "Coca-Cola": 35,
    "Sushi": 199
}

print('Enter q to stop asking:')

while True:
    name = input('Name of the dish: ')
    if name.lower() == 'q':
        break
    else:
        try:
            cost = int(input('Cost of the dish: '))
        except ValueError as ve:
            print(f"You've made a mistake: {ve}")
            continue
        else:
            menu[name] = cost


print('Словник, який відсортований по алфавіту: ')
menu1 = sorted(menu)
for key in menu1:
    a = menu.get(key, menu)
    print('{} - {}'.format(key, a))


print('Словник, який відсортований за ціною: ')

menu2 = list(menu.items())
menu2.sort(key=lambda i: i[1])
for key2 in menu2:
    print('{} - {}'.format(key2[0], key2[1]))
