def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


library_num = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108]
print("Initial array:", library_num)
heap_sort(library_num)
print("Sorted array:", library_num)
