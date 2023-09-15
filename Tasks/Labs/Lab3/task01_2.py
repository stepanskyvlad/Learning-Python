user_string = str(input("Enter your string: ").lower())


def change_string(row):
    bts = bytearray(row, 'utf-8')
    if b's' in bts:
        bts = bts.replace(b's', b'#s')
    elif b'#s' in bts:
        bts = bts.replace(b'#s', b'#')
    user_row = bts.decode('utf=8')
    print(f'Your row is: \n{user_row}')


if __name__ == '__main__':
    change_string(user_string)
