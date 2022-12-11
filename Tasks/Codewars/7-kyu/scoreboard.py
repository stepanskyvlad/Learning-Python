# Kata name: Competitive eating scoreboard

# Competitive eating scoreboard
# Chickenwings: 5 points
# Hamburgers: 3 points
# Hotdogs: 2 points
def scoreboard(who_ate_what):
    new_scoreboard = []
    for participant in who_ate_what:
        score = 0
        if 'chickenwings' in participant.keys():
            score += participant["chickenwings"] * 5
        if 'hamburgers' in participant.keys():
            score += participant["hamburgers"] * 3
        if "hotdogs" in participant.keys():
            score += participant["hotdogs"] * 2
        new_scoreboard.append(dict(name=participant["name"], score=score))
    return sorted(new_scoreboard, key=lambda x: (-x['score'], x['name']))


# another solution
def scoreboard_another(who_ate_what):
    new_scoreboard = []
    for participant in who_ate_what:
        score = participant.get("chickenwings", 0) * 5 + participant.get("hamburgers", 0) * 3 + participant.get(
            "hotdogs", 0) * 2
        new_scoreboard.append(dict(name=participant["name"], score=score))
    return sorted(new_scoreboard, key=lambda x: (-x['score'], x['name']))


print(scoreboard_another([{'name': 'Skynet'}, {'name': 'John Connor', 'hamburgers': 12, 'hotdogs': 4},
                          {'name': 'T1000', 'hamburgers': 3}, {'name': 'Kyle Reese'}]))
