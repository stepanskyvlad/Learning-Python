# Kata name: Create Phone Number
# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
def create_phone_number(n):
    n.insert(0, '(')
    n.insert(4, ')')
    n.insert(5, ' ')
    n.insert(9, '-')
    my_string = ""
    for i in n:
        my_string = my_string + str(i)
    return my_string


# best practices
def create_phone_number1(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(n))
