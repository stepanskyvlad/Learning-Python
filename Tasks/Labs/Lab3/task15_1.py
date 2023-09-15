my_string = str(input("Enter your string: "))
last_symbol = my_string[-1]
new_string = str()
for i in my_string:
    y = my_string.count(i)
    if y == 1:
        new_string += i
print(f"The string without duplicate symbols: \n{new_string}"
      f"\nLast symbol of the string --> {last_symbol}")
