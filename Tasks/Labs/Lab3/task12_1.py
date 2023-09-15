my_string = str(input("Enter cyrillic letters, please: ")).upper()
list_letters = [i for i in my_string if ord(i) in range(1030, 1170)]
sorted_list = sorted(list_letters)
new_string = ''
for i in sorted_list:
    new_string += i
print(new_string)
