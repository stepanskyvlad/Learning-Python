def linear_search(data, target):
    for ind, val in enumerate(data):
        if val == target:
            return ind  # Early exit if item is found
    return -1


if __name__ == "__main__":
    data = [4, 5, 2, 7, 1, 8]
    target = 1
    result = linear_search(data, target)
    if result == -1:
        print("Item nor found.")
    else:
        print(f"Item found at position {result}.")
