# Kata name: Tribonacci Sequence

def tribonacci(signature, n):
    if n <= 3:
        return signature[:n]
    a, b, c = signature[0], signature[1], signature[2]  # a,b,c = signature
    while len(signature) < n:
        a, b, c, = b, c, a+b+c
        signature.append(c)
    return signature


# other solutions
def tribonacci_1(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]


def tribonacci_2(s, n):
    for i in range(3, n):
        s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]


def tribonacci_3(signature, n):
    output = signature[:n]
    while len(output) < n:
        output.append(sum(output[-3:]))
    return output


print(tribonacci_1([1, 1, 1], 10))
