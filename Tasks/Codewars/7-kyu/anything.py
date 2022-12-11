# Kata name: Anything

class Thing:
    def __init__(self, something):
        self.something = something

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __le__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return True


def anything(thing):
    something = Thing(thing)
    return something


bullshit = anything("hello")
print(bullshit < "hello")
