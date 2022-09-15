doors = [False] * 101  # So we can start at door №1. We will ignore index 0

for i in range(1, 101):
    # For the second pass, i = 2, so we start at door 2, for the 3rd pass we start at door 3 etc.
    for j in range(i, 101, i):
        doors[j] = not doors[j]  # Using 'not' to invert the Boolean value

# Print out just the position of the open doors
for i in range(1, 101):
    if doors[i] is True:  # or just: "if doors[i]"
        print(i, end=", ")
