# Binary Addition
def add_binary(a, b):
    result = a + b
    return str(bin(result))[2:]


print(add_binary(5, 9))
