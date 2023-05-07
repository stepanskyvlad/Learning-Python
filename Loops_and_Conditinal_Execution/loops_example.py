# To reverse a word, push the given word to stack (letter by letter) and then, pop letters from the stack.
word = input("Please enter the word or string: ")
stack = []
for letter in word:
    stack.append(letter)
reversed_word = ''
while stack:
    reversed_word += stack.pop()
print("Reversed: {}".format(reversed_word))
