# Kata name: Build a pile of Cubes

# Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have
# a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have
# to build? findNb(1071225) --> 45 or findNb(91716553919377) --> -1
def find_nb(m):
    n = 1
    while True:
        m -= n**3
        if m == 0:
            return n
        elif m < 0:
            return -1
        n += 1


print(find_nb(91716553919377))
