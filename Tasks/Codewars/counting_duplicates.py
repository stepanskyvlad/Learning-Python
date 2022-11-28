# Counting Duplicates
def duplicate_count(text):
    counter = 0
    lower_text = text.lower()
    for i in set(lower_text):
        if lower_text.count(i) >= 2:
            counter += 1
    return counter


print(duplicate_count("aabBcde"))
