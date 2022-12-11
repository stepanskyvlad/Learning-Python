# Kata name: Building Spheres

from math import pi


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius

        self.mass = mass

        self.volume = 4 / 3 * pi * self.radius ** 3
        self.surface_area = 4 * pi * self.radius ** 2
        self.density = self.mass / self.volume

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(self.volume, 5)

    def get_surface_area(self):
        return round(self.surface_area, 5)

    def get_density(self):
        return round(self.density, 5)
