def divide(x, y):
    return x / y


def second_argument_isnt_zero(func):
    def save_version(*args):
        if args[1] == 0:
            print('Warning: second argument is zero')
            return
        return func(*args)

    return save_version


divide_safe = second_argument_isnt_zero(divide)

divide_safe(10, 0)
print(divide_safe(10, 0))
