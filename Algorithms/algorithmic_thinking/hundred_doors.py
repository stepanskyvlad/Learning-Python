# a closed door is 0, an open door is 1
doors_list = [0] * 100

for n in range(1, 101):
    ind = n-1
    loops = len(doors_list)//n
    for door in range(loops):
        if doors_list[ind]:
            doors_list[ind] = 0
        else:
            doors_list[ind] = 1
        ind += n

for i in range(1, 101):
    if doors_list[i-1] == 1:
        print(f"Door №{i} is opened")
