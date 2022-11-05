def X_O(word):
    count_x = 0
    count_o = 0
    for i in word.lower():
        if i == "x":
            count_x += 1
        elif i == "o":
            count_o += 1
    if count_x == count_o:
        return True
    elif count_x != count_o:
        return False
    elif count_x == 0 and count_o == 0:
        return True

print(X_O("ooxXm"))