class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def compare_age(self, other):
		if self.age == other[1]:
			return f"{other[0]} is the same age as me."


# Age is equal, less or greater
p1 = Person("Samuel", 24)
p2 = Person("Joel", 24)
print(print(p2))
