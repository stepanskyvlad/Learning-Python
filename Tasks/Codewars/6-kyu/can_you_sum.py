# Can you sum?
def f(n):
    # the hard way
    # Sum of (a^k * k^a) (for k=0 to n) = sum_(k=0)^n a^k k^a = Li_(-a)(a) - a^(n + 1) Φ(a, -a, n + 1)
    # https://fredrikj.net/blog/2022/02/computing-the-lerch-transcendent/
    # https://github.com/mpmath/mpmath/blob/master/mpmath/functions/theta.py

    # the easy way
    # A036800 -> a(n) = -6 + 2^(n+1)*(3 - 2*n + n^2)
    M = int(1e9) + 7
    return (-6 + pow(2, n + 1, M) * (3 - 2 * n + pow(n, 2, M))) % M


print(f(420))
