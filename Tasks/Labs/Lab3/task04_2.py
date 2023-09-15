def user_input():
    user_str = input("Enter your string: ")
    return user_str


def change_line(user_str):
    first_half = bytearray(user_str[:round(len(user_str)/2)], 'utf-8').replace(b':', b'.')
    second_half = bytearray(user_str[round(len(user_str)/2):], 'utf-8').replace(b'!', b'.')
    changed_line = (first_half+second_half).decode('utf-8')
    return changed_line


def print_result(result):
    print(f"Your result is: \n{result}")


def main():
    user_str = user_input()
    result = change_line(user_str)
    print_result(result)


if '__main__' == __name__:
    main()
