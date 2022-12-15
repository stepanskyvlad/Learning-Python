myList = [{'age': 132}, {'age': 22}, {'age': 32}, {'age': 13}]
myList.sort(key=lambda e: e["age"], reverse=True)
print(myList)

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
to_add = [6, 7, 8, 9]
list1.append(to_add)
list2.extend(to_add)
print(list1)
print(list2)
