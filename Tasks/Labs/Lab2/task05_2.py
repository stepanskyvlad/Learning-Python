my_list = []
for i in range(4):
    x = float(input("Enter a number: "))
    my_list.append(x)

pos_list = [i**2 for i in my_list if i > 0]
pos_result = sum(pos_list)
neg_list = [i for i in my_list if i < 0]
neg_result = sum(neg_list)**2

print(f"The sum of the positive numbers is {pos_result} \nThe sum of the negative numbers is {neg_result}")
if neg_result > pos_result:
    print("The sum of the negative numbers is greater than the positive one")
elif pos_result > neg_result:
    print("The sum of the positive numbers is greater than the negative one")
else:
    print("The sum of the negative numbers is equal to the positive one")
