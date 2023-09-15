first_string = str(input("Enter your first string, please: "))
second_string = str(input("Enter your second string, please: "))
new_string = ''
x = 0
while x < len(first_string):
    new_string += first_string[x]
    new_string += second_string[x]
    x += 1
print(f"{new_string}")
