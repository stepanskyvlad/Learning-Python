class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color


def init(self, *a):
    for i, n in enumerate(self.lst):
        if type(a[i]) == str:
            exec(f'self.{n} = "{a[i]}"')
        else:
            exec(f'self.{n} = {a[i]}')


def make_class(*args):
    return type('make_class', (), {"lst": args, "__init__": init})


Animal2 = make_class("name", "species", "age", "health", "weight", "color")

dog1 = Animal("Bob", "Dog", 5, "good", "50lb", "brown")
dog2 = Animal2("Bob", "Dog", 5, "good", "50lb", "brown")

print(dog1.name, dog2.name)


# another solution
def make_class_another(*atts):
    class Class(object):
        def __init__(self, *args):
            for att, arg in zip(atts, args):
                setattr(self, att, arg)

    return Class
