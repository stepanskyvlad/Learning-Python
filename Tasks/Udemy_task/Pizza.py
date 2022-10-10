class Pizza:
    # static counter
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])


p1 = Pizza(['ham', 'bacon'])
p2 = Pizza.garden_feast()
p3 = Pizza.hawaiian()
p4 = Pizza(['beef', 'olives'])

print(Pizza.order)
print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
