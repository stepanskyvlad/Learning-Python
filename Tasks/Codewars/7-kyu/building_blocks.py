# Kata name: Building blocks

class Block:
    def __init__(self, lst: list):
        self.width = lst[0]
        self.length = lst[1]
        self.height = lst[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.height * self.length

    def get_surface_area(self):
        return (2*self.width * self.height) + (2*self.height * self.length) + (2*self.width * self.length)
