user_input = str(input("Enter your string: "))


def change_string(row):
    """Перед кожною великою латинською
     літерою поставити крапку і пробіл"""
    new_string = ''
    for i in row:
        if ord(i) in range(65, 91):
            new_string += '. ' + i
        else:
            new_string += i
    print(new_string)


if __name__ == "__main__":
    change_string(user_input)
