# There are 3 teams that take part in the darts' competition. Each team comprises 4 participants. Each participant has
# 3 attempts. The number of points that each participant gets for one throw is entered from a keyboard. The maximum
# number of points for 1 attempt is 60. Display the winner (i.e. the number of the participant with the biggest
# number of points and his/her result) from each team. The participant of which team showed the best result?
team_count = 3
players_count = 4
team_results = []

max_team_number = winner_number = max_result = 0
for team_number in range(1, team_count + 1):
    team_result = []
    max_for_player = max_player_number = 0

    for player_number in range(1, players_count + 1):
        player_score = input("Enter {} team {} player result: ".format(
            team_number,
            player_number,
        )).split()
        player_sum = sum([int(score) for score in player_score])
        if player_sum > max_for_player:
            max_for_player, max_player_number = player_sum, player_number

    print("Team {}. The winner is the player {} with the score of {}".format(
        team_number,
        max_player_number,
        max_for_player,
    ))

    if max_for_player > max_result:
        max_team_number, winner_number = team_number, max_player_number
        max_result = max_for_player

print("The best result was shown by player {} of the team {} with the score of {}".format(
    winner_number,
    max_team_number,
    max_result,
))
"""
Output:
Enter 1 team 1 player result: 20
Enter 1 team 2 player result: 80
Enter 1 team 3 player result: 100
Enter 1 team 4 player result: 100
Team 1. The winner is the player 3 with the score of 100
Enter 2 team 1 player result: 70
Enter 2 team 2 player result: 40
Enter 2 team 3 player result: 20
Enter 2 team 4 player result: 120
Team 2. The winner is the player 4 with the score of 120
Enter 3 team 1 player result: 20
Enter 3 team 2 player result: 30
Enter 3 team 3 player result: 40
Enter 3 team 4 player result: 140
Team 3. The winner is the player 4 with the score of 140
The best result was shown by player 4 of the team 3 with the score of 140
"""