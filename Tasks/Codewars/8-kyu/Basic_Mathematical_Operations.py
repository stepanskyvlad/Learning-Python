# Kata name: Basic Mathematical Operations

# my solution
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2


# other solutions
def basic_op_1(o, a, b):
    # The get() method is for dictionaries. In this case, o is the key.
    # When get(o) is called, it will return the value that corresponds
    # with the key, which is then returned by the basic_op() function.
    return {'+': a + b,
            '-': a - b,
            '*': a * b,
            '/': a / b}.get(o)


def basic_op_2(operator, value1, value2):
    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)


def basic_op_3(operator, value1, value2):
    return {"+": value1 + value2,
            "-": value1 - value2,
            "*": value1 * value2,
            "/": value1 / value2,
            }[operator]


def basic_op_4(operator: str, value1: int, value2: int) -> int:
    match operator:
        case '+':
            return value1 + value2
        case '-':
            return value1 - value2
        case '*':
            return value1 * value2
        case '/':
            return value1 / value2
        case _:
            raise ValueError('Wrong Operator')


print(basic_op_4('/', 6, 5))
