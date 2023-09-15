user_input = str(input("Enter your string: "))


def change_row(row):
    new_string = row.replace('№', 'номер по порядку ')
    print(new_string)


if __name__ == '__main__':
    change_row(user_input)
