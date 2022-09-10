jpeg = [120, 3, 25, 255, 0, 100]
with open("bytefile.bin", 'w+b') as file:
    file.write(bytes(jpeg))

with open('bytefile.bin', 'rb') as file:
    data = file.read()
    print(data)
    for b in data:
        print(int(b))
