str_in_bytes = bytearray(input('Enter your string: '), 'utf-8')
user_input = str_in_bytes.decode('utf-8')
not_letters = ''
for i in user_input:
    if not i.isalpha():
        not_letters += i
print("{}".format(len(not_letters)))
