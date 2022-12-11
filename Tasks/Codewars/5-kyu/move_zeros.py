# Kata name: Moving Zeros To The End
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
def move_zeros(lst):
    for i in range(lst.count(0)):
        lst.remove(0)
        lst.append(0)
    return lst


# another solution
def move_zeros_1(array):
    return [x for x in array if x] + [0]*array.count(0)


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
