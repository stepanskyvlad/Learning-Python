# Kata name: Sum of the first nth term of Series

# Your task is to write a function which returns the sum of following series upto nth term(parameter).
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
def series_sum(n):
    result, denominator = 0, 1
    for i in range(n):
        result += 1/denominator
        denominator += 3
    return f"{result:.2f}"


# another solution
def series_sum_1(n):
    result = 0
    for x in range(n):
        result += 1/(1 + x * 3)
    return "{:.2f}".format(result)


print(series_sum(5))
