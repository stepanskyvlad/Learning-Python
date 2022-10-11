def is_full_house(lst: list):
    unique = list(set(lst))
    if len(unique) == 2:
        if (lst.count(unique[0]) == 2 and lst.count(unique[1]) == 3) or (
                lst.count(unique[0]) == 3 and lst.count(unique[1]) == 2):
            return True
    return False


# another solution
def is_full_house_1(hand):
    return all([hand.count(i) >= 2 for i in hand])


print(is_full_house_1(['A', 'A', 'K', 'K', 'K']))
print(is_full_house_1(['A', 'A', 'K', 'K', '2']))
