def check_sequence(sequence: list):
    if sequence == sorted(set(sequence)):
        return 1
    elif sequence == sorted(set(sequence), reverse=True):
        return -1
    else:
        return 0


if __name__ == "__main__":
    print(check_sequence([1, 2, 3]))
    print(check_sequence([3, 2, 1]))
    print(check_sequence([1, 1, 2]))


