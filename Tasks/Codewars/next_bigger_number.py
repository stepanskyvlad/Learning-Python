# Create a function that takes a positive integer and
# returns the next bigger number that can be formed by rearranging its digits. For example:
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
def next_bigger(n):
    ind = 0
    my_list = list(str(n))
    for i in range(len(my_list))[::-1]:
        if ind == 0:
            ind = int(my_list[i])
        elif ind <= int(my_list[i]):
            ind = int(my_list[i])
        else:
            # a value of the target digit
            to_change = my_list[i]
            # an index of the target digit
            ind_to_change = i
            for j in sorted(my_list[ind_to_change:]):
                if int(j) > int(to_change):
                    # a value of the digit with what we swap the target digit
                    with_what = j
                    for x in range(len(my_list))[::-1]:
                        # an index of the digit with what we swap the target digit
                        if my_list[x] == with_what:
                            ind_with_what = x
                            my_list[ind_to_change], my_list[ind_with_what] = my_list[ind_with_what], my_list[ind_to_change]
                            new_list = my_list[:ind_to_change + 1] + sorted(my_list[ind_to_change + 1:])
                            new_number = int(''.join(new_list))
                            return new_number
    return -1


print(next_bigger(14))
