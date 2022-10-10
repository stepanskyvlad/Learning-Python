# walrus-operator - " := "

# walrus = False
# print(walrus)

print(walrus := True)
print(type(walrus))

# rows = input('Enter the number of rows: ')
# for i in range(int(rows)):
#     print('*' * (i+1))
# print(f"number of rows: {rows}")

for i in range(int(rows := int(input("Enter the number of rows: ")))):
    print('*' * (i+1))
print(f"number of rows: {rows}")


def read_file1(fp):
    while True:
        line = fp.readline()
        if not line:
            break

        split_line = line.split(';')
        print(split_line)


def read_file2(fp):
    while line := fp.readline():
        if not line:
            break

        split_line = line.split(';')
        print(split_line)
