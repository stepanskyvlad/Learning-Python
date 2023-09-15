my_string = str(input("Enter your string: "))
new_string = ""
for i in my_string:
    # Кириличні букви заміняються на зірочку
    if ord(i) in range(1040, 1170):
        new_string += '*'
    else:
        new_string += i
print('{}'.format(new_string))
