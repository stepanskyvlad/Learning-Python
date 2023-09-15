my_string = str(input("Would you be so kind to write a string?: "))
one_symbol = str(input("Can you enter a symbol, please? :"))
new_string = ''
for i in my_string:
    if i not in one_symbol:
        new_string += i
print(f"Your new string is: \n{new_string}")
