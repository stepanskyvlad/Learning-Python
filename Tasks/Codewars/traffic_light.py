# Thinkful - Logic Drills: Traffic light
def update_light(current):
    match current:
        case "green":
            return "yellow"
        case "yellow":
            return "red"
        case "red":
            return "green"
        case _:
            return


# other solution
def update_light_1(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]


