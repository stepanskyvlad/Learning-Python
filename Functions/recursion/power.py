def power(num, pwr):
    if pwr == 0:
        return 1
    return num * power(num, pwr-1)


print("{} to the power of {} is equal to {}".format(10, 0, power(10, 0)))
print("{} to the power of {} is equal to {}".format(2, 5, power(2, 5)))
