from dataclasses import dataclass


@dataclass
class PlayingCard:
    rank: str
    suit: str


if __name__ == '__main__':
    queen_of_hearts = PlayingCard('Q', 'Hearts')
    print(queen_of_hearts.rank)
