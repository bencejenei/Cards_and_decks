from dataclasses import dataclass, field
from typing import List
from random import sample

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck() -> list:
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (SUITS.index(self.suit))

    def __str__(self):
        return f"{self.rank} {self.suit}"

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')


@dataclass()
class CustomDeck:
    cards: List[PlayingCard]

    def __str__(self, cards=None):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


@dataclass
class FullDeck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)
    
    def __str__(self, cards=None):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


if __name__ == '__main__':
    print(FullDeck())

    hand = (CustomDeck(sorted(sample(make_french_deck(), k=10))))
    print(f"\n{hand}")
