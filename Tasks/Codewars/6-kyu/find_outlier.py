def find_outlier(integers):
    mydict = {"odd": [], "even": []}
    for integer in integers:
        if integer % 2:
            mydict["odd"].append(integer)
        else:
            mydict["even"].append(integer)
        if len(mydict['odd']) > 1 and len(mydict["even"]) == 1:
            return mydict['even'][0]
        elif len(mydict['even']) > 1 and len(mydict["odd"]) == 1:
            return mydict['odd'][0]


print(find_outlier([2, 6, 8, 2, -66, 34, -35, 66, 700, 1002, -84, 10, 4]))  # --> -35 (the only even number)
