class Dog:
    _legs =4
    def __init__(self, name):
        self.name = name

    def get_legs(self):
        return self._legs

    def speak(self):
        print(self.name + 'says: Bark')

class Chihuahua(Dog):
    def speak(self):
        print(f"{self.name} says: Yap yap yap")

    def wag_tail(self):
        print('Vigorous wagging')

dog = Chihuahua('Roxy')
dog.speak()
dog.wag_tail()

mydog = Dog('Rover')
mydog.speak()

class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)

unique_list = UniqueList()
unique_list.append(1)
unique_list.append(1)
unique_list.append(2)

print(unique_list)
