# I must use bytes according to the task
def get_binary_num():
    while True:
        binary = bytes(input("Enter your binary number: "), 'utf-8')
        for i in binary:
            if i != 49 and i != 48:  # 48 and 49 - zero and one in bytes
                print(f"Please, try again.")
                break
        else:
            de_binary = binary.decode('utf8')
            return de_binary


def get_decimal(num):
    decimal_number = int(num, 2)
    return decimal_number


def main():
    binary_num = get_binary_num()
    decimal_num = get_decimal(binary_num)
    print(f"Your binary number in decimal system is {decimal_num}")


if __name__ == '__main__':
    main()
