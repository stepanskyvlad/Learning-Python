my_string = str(input("Enter latin letters, please: ")).lower()
letters = [ord(i) for i in my_string if ord(i) in range(97, 123)]
list_letters = sorted(letters)
new_string = ''
for i in list_letters:
    new_string += chr(i)
print("There`re your lower latin letters: \n{}".format(new_string))
