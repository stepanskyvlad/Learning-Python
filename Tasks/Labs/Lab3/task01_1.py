my_string = str(input("Enter your string: "))
my_list = my_string.split()
new_string = ''
for i in my_list:
    new_string += i + ' '
print(new_string.rstrip())
