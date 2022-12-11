# Find the next perfect square!
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    number = sq ** (1/2)
    if round(number, 3) == int(number):
        return int((number+1) ** 2)
    return -1


# other solutions
def find_next_square_1(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1


def find_next_square_2(sq):
    x = sq**0.5
    return -1 if x % 1 else (x+1)**2


print(find_next_square(144))
