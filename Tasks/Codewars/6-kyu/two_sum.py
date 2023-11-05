# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
def two_sum(numbers, target):
    seen = {}  # Initialize an empty dictionary

    for i, num in enumerate(numbers):
        diff = target - num  # Calculate the difference

        if diff in seen:
            return (seen[diff], i)  # Return indices if difference is in the dictionary

        seen[num] = i  # Add current element to the dictionary

    # If no pair is found, you can return None or raise an exception
    return None


print(two_sum([4, 17, 5, 4, 7, 25, 19, 28, 0, 17, 9], 23))  # returns (0, 3)
