import random
from typing import Optional, Any, Union, List, Tuple, Dict, Iterable


class Character:

    def __init__(self, armor: int, power: int):
        self.power = power
        self.armor = armor
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    # можна вказати, який тип повертає функція
    def is_alive(self) -> bool:
        return self.health > 0


c1 = Character(10, 20)
c1.hit(20)

amount: int  # we can write only int
amount = None  # Expected type 'int', got 'None' instead

price: Optional[int]
price = None  # now we can write int or None
price = 'abc'  # Expected type 'int | None', got 'str' instead

attack: Any = 1  # we can write any type
attack = 'h1'

# several types of data can be passed to a variable
length = Union[int, float]
length = 1
length = 1.2

quotes: List[int] = [1]
quotes.append('abcd')  # Expected type 'int' (matched generic type '_T'), got 'str' instead

player: Tuple[str, int] = ("Carlsen", 2800)

changes_in_rating: Tuple[int, ...]  # кортеж складається з кучі елементів певного типу
changes_in_rating = (1, 2, 3, 4, 5)
changes_in_rating = (1, 'a')  # Expected type 'tuple[int, ...]', got 'tuple[int, str]' instead

chess_players: Dict[str, int] = {'Carlsen': 2800}


# можна вказати, що із функції повертається об'єкт, що ітерується
def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)
