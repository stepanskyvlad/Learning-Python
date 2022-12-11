# Kata name: Count by X

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return list(range(x, x*(n+1), x))


print(count_by(2, 10))
