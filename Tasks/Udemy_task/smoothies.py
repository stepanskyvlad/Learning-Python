prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
          "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
          "Pineapple": 3.5}


class Beverage:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        cost = sum(prices[fruit] for fruit in self.ingredients)
        return f"${cost:.2f}"

    def get_price(self):
        price = sum(prices[fruit] for fruit in self.ingredients) * 2.5
        return f"${price:.2f}"

    def get_name(self):
        self.ingredients.sort()
        for i in range(len(self.ingredients)):
            self.ingredients[i] = self.ingredients[i].replace('berries', 'berry')
        if len(self.ingredients) == 1:
            return f"{self.ingredients[0]} Smoothie"
        else:
            return f"{' '.join(self.ingredients)} Fusion"


s1 = Beverage(["Banana"])
print(s1.ingredients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())
s2 = Beverage(["Raspberries", "Strawberries", "Blueberries"])
print(s2.ingredients)
print(s2.get_cost())
print(s2.get_price())
print(s2.get_name())


# another solution
class BeverageAnother:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        return f"${self.cost:.2f}"

    def get_price(self):
        return f"${self.price:.2f}"

    def get_name(self):
        lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
        return f'{" ".join(lst)} {"Fusion" if len(lst) > 1 else "Smoothie"}'

