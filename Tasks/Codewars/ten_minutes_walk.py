# Take a Ten Minutes Walk
# My solutions
from collections import Counter


def is_valid_walk(walk):
    if len(walk) == 10:
        ns = 0
        we = 0
        for i in walk:
            match i:
                case 'n':
                    ns += 1
                case 's':
                    ns -= 1
                case 'w':
                    we -= 1
                case 'e':
                    we += 1
        if ns == 0 and we == 0:
            return True
    return False


def is_valid_walk_1(walk):
    if len(walk) != 10:
        return False
    my_dict = {'n': 0, 's': 0, 'w': 0, 'e': 0}
    for i in walk:
        my_dict[i] += 1
    return all((my_dict['n'] == my_dict['s'], my_dict['w'] == my_dict['e']))


# other solutions
def is_valid_walk_2(walk):
    if len(walk) == 10:
        walk_map = Counter(walk)
        return walk_map['n'] == walk_map['s'] and walk_map['e'] == walk_map['w']
    return False


print(is_valid_walk_1(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
