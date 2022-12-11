# Kata name: Recursion 101

def solve(a, b):
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2 * b:
        a = a - 2 * b
        return solve(a, b)
    elif b >= 2 * a:
        b = b - 2 * a
        return solve(a, b)
    else:
        return [a, b]


# not recursion
def solve_1(a, b):
    while a and b:
        if a >= b * 2:
            a %= 2 * b
        elif b >= a * 2:
            b %= 2 * a
        else:
            break
    return [a, b]


print(solve(2, 10))
