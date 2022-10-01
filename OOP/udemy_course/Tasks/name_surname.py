class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.initials = f"{self.first_name[0]}.{self.last_name[0]}"


n = Name("vlad", "yarema")
print(n.first_name)
print(n.last_name)
print(n.full_name)
print(n.initials)

