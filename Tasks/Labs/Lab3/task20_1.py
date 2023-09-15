user_input = str(input("Enter your string: "))


def change_string(row):
    new_string = row.replace('+-', '0')
    print(new_string)


if __name__ == "__main__":
    change_string(user_input)
