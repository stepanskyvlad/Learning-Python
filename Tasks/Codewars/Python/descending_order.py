# Your task is to make a function that can take any non-negative integer as an argument and return it with its
# digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Input: 42145 Output: 54421
def descending_order(num):
    sorted_digits = sorted(list(str(num)), reverse=True)
    max_number = int(''.join(sorted_digits))
    return max_number


number = 150
print(descending_order(number))
