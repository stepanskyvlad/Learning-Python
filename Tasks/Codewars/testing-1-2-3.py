# Testing 1-2-3
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
# my solution
def number(lines):
    return [f"{n}: {string}" for n, string in zip(range(1, len(lines) + 1), lines)]


# another solution
def number_1(lines):
    return [f"{n}: {ligne}" for n, ligne in enumerate(lines, 1)]  # 1 - from what number you should start count


print(number_1(['a', 'b', 'c']))
