def bubble_sort(arr):
    count = 0
    need_iteration = 'true'
    while need_iteration == 'true':
        need_iteration = 'false'
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    need_iteration = 'true'
                    count += 1
    print("The number of permutations is", count)


library_num = [3, 4, 5, 2, 1]
print("Initial array:", library_num)
bubble_sort(library_num)
print("Sorted array:", library_num)
