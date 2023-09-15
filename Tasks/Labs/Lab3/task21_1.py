a = input("Введіть рядок: ")
b = str()
for i in a:
  if i == 'я':
    b += " "
  else:
    b += chr(ord(i)+1)
print("{0}".format(b))
