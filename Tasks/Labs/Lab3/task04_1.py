my_string = str(input("Enter your string, please: "))
new_string = ''
for i in my_string:
    # Видаляє всі букви латиниці
    if ord(i) not in range(65, 91) and ord(i) not in range(97, 123):
        new_string += i
print("\n{} - мій рядок".format(new_string))
