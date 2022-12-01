# Sum Mixed Array
def sum_mix(arr):
    return sum(int(i) for i in arr)


# other solutions
def sum_mix_1(arr):
    return sum(map(int, arr))


print(sum_mix_1([1, 2, 3, '4', '5']))
