# Kata name: Rock Paper Scissors!

def rps(p1, p2):
    my_dict = {("scissors", "paper"): 1,
               ("scissors", "rock"): 2,
               ("rock", "scissors"): 1,
               ("rock", "paper"): 2,
               ("paper", "rock"): 1,
               ("paper", "scissors"): 2}
    if p1 == p2:
        return "Draw!"
    winner = my_dict[(p1, p2)]
    return f"Player {winner} won!"


# other solutions
def rps_1(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


def rps_2(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


print(rps('rock', 'scissors'))
