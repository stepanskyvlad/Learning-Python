def probability(lst, num):
    count = 0
    for i in lst:
        if i >= num:
            count += 1
    per = round(100*(count/len(lst)), 1)
    return per


print(probability([7, 4, 17, 14, 12, 3], 16))
