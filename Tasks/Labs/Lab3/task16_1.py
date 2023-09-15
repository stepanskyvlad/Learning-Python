def sorting(your_string):
    str_in_bytes = bytearray(your_string, 'utf-8')
    my_list = sorted([i for i in str_in_bytes])
    str_in_words = ''
    for i in my_list:
        str_in_words += chr(i)
    print(str_in_words)


my_string = str(input("Enter your string: "))
sorting(my_string)


def new_sorting(row):
    new_row = ''.join(sorted(row, reverse=True))
    print(new_row)


some_word = str(input("Enter a word: "))
new_sorting(some_word)
