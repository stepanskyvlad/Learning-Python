user_input = str(input("Enter your string: "))


def change_string(row):
    new_string = ' '.join(row)
    print(f"It is the new string: \n{new_string}")


if __name__ == "__main__":
    change_string(user_input)
