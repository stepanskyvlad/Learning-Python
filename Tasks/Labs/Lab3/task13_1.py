my_string = str(input("Enter your string, please: "))
new_string = ''
x = 0
while x < len(my_string):
    try:
        new_string += my_string[x+1]
        new_string += my_string[x]
        x += 2
    except IndexError as ie:
        print(f"There`s a problem - {ie}")
        new_string += my_string[x]
        break
print(new_string)
