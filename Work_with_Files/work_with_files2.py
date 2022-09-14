with open("sample.txt", 'w') as file:
    file.write("Name|Phone\n"
               "John;1234\n"
               "Bob;5678\n"
               "Alice;9432\n")

file = open('sample.txt')
print(file)
# <_io.TextIOWrapper name='sample.txt' mode='r' encoding='cp1252'>
data = file.read()
print(type(data))
print(data)
# Name|PhoneJohn;1234Bob;5678Alice;9432
print(file.read())
# no information, use seek() to move the cursor
file.seek(0)
print(file.read())

file.seek(0)
lines = file.readlines()
print(type(lines))  # <class 'list'>
print(lines)
# ['Name|Phone\n', 'John;1234\n', 'Bob;5678\n', 'Alice;9432\n']
print(len(lines))  # 4
file.seek(0)

sample_file = open(r'C:\Users\vladyarema\PycharmProjects\Learning-Python\Work_with_Files\work_with_files2.py')
new_data = file.read()
print(new_data)
sample_file.close()
file.close()
# check if the files are closed
print(sample_file.closed)
print(file.closed)

# append information in existing file
with open('sample.txt', mode='a') as sample_file:
    sample_file.write('Eric;7639')

with open('sample.txt', mode='r') as sample_file:
    print(sample_file.read())

# append and read information
with open("sample.txt", mode='r+') as sample_file:
    sample_file.seek(0, 2)  # move cursor no the end of the file
    sample_file.write('\nToub;5627')
    sample_file.seek(0)
    print(sample_file.read())

