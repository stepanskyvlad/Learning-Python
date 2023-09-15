my_line = str(input("Enter your string: "))
# we changed '!' to '!?'
if '!' in my_line:
    my_line = my_line.replace('!', '!?')
print(f"New string is: \n{my_line}")
