# Kata name: Simple fibonacci strings

def solve(n):
    a, b = '0', '01'
    for _ in range(n):
        a, b = b, b + a
    return a


print(solve(3))
