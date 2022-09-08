class Wall:
    def __init__(self, material, height):
        self.material = material
        self.height = height

    def __str__(self):
        return "Material is '{}', height = {} ft.".format(self.material,
                                                          self.height)


class Furniture:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return "name = '{}', cost = {}$".format(self.name, self.cost)


class Apartment:
    def __init__(self, street, apartment_no, material, height, furniture):
        self.street = street
        self.apartment_no = apartment_no
        self.walls = Wall(material, height)
        self.furniture = furniture

    def __str__(self):
        return "The address is '{}'St {}, walls {}, furniture=[\n{}]".format(
            self.street,
            self.apartment_no,
            self.walls,
            '\n'.join(str(element) for element in self.furniture),
        )

    def get_total_furniture_cost(self):
        total_cost = 0
        for element in self.furniture:
            total_cost += element.cost
        return total_cost


if __name__ == "__main__":
    furniture = [Furniture("bed", 150), Furniture("cupboard", 250),
                 Furniture("table", 35), Furniture("armchair", 80)]
    flat1 = Apartment("Bronco", 3050, "brick", 23, furniture)
    print("Information about the first apartment:", flat1)
    print("Total furniture cost is {}$".format(flat1.get_total_furniture_cost()))
