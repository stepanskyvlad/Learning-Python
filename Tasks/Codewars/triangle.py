# Is this a triangle?
def is_triangle(a, b, c):
    return (a + b) > c and (b + c) > a and (c + a) > b


# other solutions
def is_triangle_1(a, b, c):
    return all([a + b > c, a + c > b, b + c > a])


# clever
def is_triangle_2(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c
