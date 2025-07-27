from app.card_deck import *
'''import pytest'''

def test_card():
    """4-point test"""
    card = Card(suit="Clubs", rank="5")
    assert card.suit == "Clubs"
    assert card.rank == "5"


def test_show():
    """4-point test"""
    card = Card(suit="Clubs", rank="5")
    assert card.show() == "5 of Clubs"


def test_deck():
    """4-point test"""
    deck = Deck()
    assert len(deck.cards) == 52
    assert all([isinstance(c, Card) for c in deck.cards])


def test_deal():
    """4-point test"""
    deck = Deck()
    card1 = deck.deal()
    assert isinstance(card1, Card)
    assert len(deck.cards) == 51
    card2 = deck.deal()
    assert isinstance(card2, Card)
    assert len(deck.cards) == 50
    assert card1.show() != card2.show()


def test_shuffle():
    """4-point test"""
    deck1 = Deck()
    assert len(deck1.cards) == 52
    deck2 = Deck()
    deck1.shuffle()
    deck2.shuffle()
    same = sum([deck1.cards[i].show() == deck2.cards[i].show() for i in range(52)])
    assert same < 40
