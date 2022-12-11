# Kata name: Total amount of points

def points(games):
    counter = 0
    for game in games:
        if game[0] > game[2]:
            counter += 3
        elif game[0] == game[2]:
            counter += 1
    return counter
