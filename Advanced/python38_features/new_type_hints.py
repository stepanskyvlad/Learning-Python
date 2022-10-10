from typing import Literal, Final, final, Dict, Any, TypedDict


def open_file(file, mode: Literal['r', 'w']):
    pass


open_file(r"C:\file.txt", 'v')

# we can create a constant using typing
pi: Final = 3.14

pi = 1.2


# we can disallow class inheritance
@final
class Dog:
    def __init__(self):
        self.paws = 4
        self.health = 100
        self.sound = 'woof-woof'

    def bark(self):
        print(self.sound)


class SuperDog(Dog):  # -> 'Dog' is marked as '@final' and should not be subclassed
    def __init__(self):
        super().__init__()
        self.health = 200
        self.sound = 'super-woof'


dog = SuperDog()
print(dog.health)
dog.bark()

dict_result: Dict[str, Any] = {'word': "hello", "count": 5, "comment": 'an interesting word'}
dict_result['comment'] = 123  # we not have expected type for a certain key


class WordStat(TypedDict):
    word:  str
    count: int
    comment: str


dict_result_new: WordStat = {'word': 'hello', 'count': 5, 'comment': 'a very interesting word'}
dict_result_new['word'] = 33  # Expected type 'str', got 'int' instead

