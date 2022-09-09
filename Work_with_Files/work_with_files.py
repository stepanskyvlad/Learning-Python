f = open("10_01_file.txt", 'r')
for line in f.readlines():
    print(line.strip())


f = open("10_01_output.txt", 'w')
print(f)
f.write("Line 1\n")
f.write("Line 2\n")
f.close()
f = open("10_01_output.txt", 'a')
f.write('Line 3\n')
f.write('Line 4\n')
f.close()

with open("10_01_output.txt", 'a') as file:
    file.write("Add some staff\n")
    file.write("Add another staff\n")
    