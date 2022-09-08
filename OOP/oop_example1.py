class Building:
    wall_material = "brick"

    def __init__(self, purpose, address, floors_number):
        self.purpose = purpose
        self.address = address
        self.floors_number = floors_number

    def __str__(self):
        return f"The purpose is {self.purpose}. Address: {self.address}. Number of floors: {self.floors_number} and " \
               f"wall material is {self.wall_material} "


cafe = Building("organization of recreation", "London, Baker Street", 2)
print("Information about the cafe:")
print(cafe)
shop = Building("organization of shopping", "London, Crawford street", 1)
print("Information about the shop:")
print(shop)
