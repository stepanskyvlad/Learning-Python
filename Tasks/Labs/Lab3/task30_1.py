def get_string():
    line = input("Enter a string: ")
    return line


def change_string(line):
    if 'sin' in line:
        line = line.replace('sin', 'sin()')
    if 'cos' in line:
        line = line.replace('cos', 'cos()')
    if 'log' in line:
        line = line.replace('log', 'log()')
    print("{}".format(line))


def main():
    line = get_string()
    change_string(line)


if __name__ == "__main__":
    main()
