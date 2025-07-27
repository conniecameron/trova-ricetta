import random


class Card:

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def show(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        """standard Poker deck"""
        self.suits = ('Clubs', 'Hearts', 'Spades', 'Diamonds')
        self.ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10',
             'J', 'Q', 'K', 'A')

        """Create the deck using list comprehension"""
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        #self.cards: [Card]

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal(self) -> Card:
        """removes and returns the last item in the list"""
        return self.cards.pop()
