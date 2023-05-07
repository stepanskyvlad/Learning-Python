def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(http_error(213))
# Output: Something's wrong with the internet

# array
item = ['day', 'dance']
match item:
    case ['evening', action]:
        print(f'You almost finished the day! Now {action}!')
    case [time, action]:
        print(f'Good {time}! It is time to {action}!')
    case _:
        print('The time is invalid.')

# dict
item = {"time": "evening", "action": "play"}
match item:
    case {"time": "evening", "action": action}:
        print(f"You almost finished the day! Now {action}!")
    case {"time": time, "action": action}:
        print(f"Good {time}! It is time to {action}!")
    case _:
        print("The time is invalid.")


# obj
class MyClass:
    __match_args__ = ('time', 'action')

    def __init__(self, time, action):
        self.time = time
        self.action = action


item = MyClass("evening", "work")
match item:
    case MyClass(time="evening", action="relax"):
        print(f"You almost finished the day!")
    case MyClass(time, action):
        print(f"Good {time}! It is time to {action}!")
    case _:
        print("The time is invalid.")
