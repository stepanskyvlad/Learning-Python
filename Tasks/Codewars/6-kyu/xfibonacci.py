# Kata Name: Fibonacci, Tribonacci and friends

def Xbonacci(signature, n):
    new_signature = signature.copy()
    while len(new_signature) < n:
        new_signature.append(sum(new_signature[-len(signature):]))
    return new_signature[:n]


# other solutions
def Xbonacci_1(signature, n):
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output


def Xbonacci_2(signature, n):
    x = len(signature)
    result = signature[:n]
    for i in range(n - x):
        result.append(sum(result[i: i + x]))
    return result


print(Xbonacci([0, 1], 10))
