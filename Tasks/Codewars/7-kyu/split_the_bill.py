# Kata name: Split The Bill

# It's tricky keeping track of who is owed what when spending money in a group. Write a function to balance the books.
# The function should take one parameter: an object/dict with two or more name-value pairs which represent the members
# of the group and the amount spent by each. The function should return an object/dict with the same names,
# showing how much money the members should pay or receive.
def split_the_bill(group: dict):
    average_bill = sum([group[person] for person in group.keys()]) / len(group)
    for person in group.keys():
        group[person] = round(group[person] - average_bill, 2)
    return group


# another solution
def split_the_bill_1(x):
    diff = sum(x.values())/float(len(x))
    return {k: round(x[k]-diff, 2) for k in x}


print(split_the_bill({'A': -17.200000000000003, 'B': -32.2, 'C': -47.2, 'D': 95.8, 'E': 0.7999999999999972}))
