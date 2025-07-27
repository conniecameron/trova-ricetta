[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gXkrshpW)
# Ling508 Programming Assignment Week 2
Programming Assignment for LING 508 Week 2

In this assignment, you will create 2 classes to implement a generic deck of cards. We're modeling these objects based on
the real-world objects, so the properties of the real-world objects can and should guide your development of these
software objects. Your code should be written in `app/card_deck.py`. Remember that you should be approaching this task
with the mindset of test-driven development, so make sure you're looking at the tests before you even start to code, and
writing the code in order to pass the given tests. Have a look at the tests in `tests/test_card_deck.py` for more information. 

The first class is `Card`, which has 2 attributes: `suit` and `rank`. 
`Card` also has a method `show() -> str` which will return a string with the format "<*rank*> of <*suit*>", e.g. "5 of Clubs", as specified in the tests.

The second class is `Deck`. 
The `Deck` should consist of 52 cards, each an instance of the class `Card`. 
The cards are the 13 ranks "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", and "A" for each of the 4 suits 
"Clubs", "Hearts", "Spades", and "Diamonds".

> *Hint: If the rank order and suit order should be a constant property of a given `Deck` object, it might make sense to
  store them as
  [constants that are accessible as part of that class](https://realpython.com/python-constants/#putting-constants-together-with-related-code).
  A standard Poker deck might have different such constants from a deck for, say, [Sabacc](https://starwars.fandom.com/wiki/Sabacc#Cards). These
  values (the ranks and suits) might change, but the underlying logic of a `Deck` object and a `Card` object would remain the same. You could
  accomplish that either by changing out the constants depending on what kind of deck it is, or you could define a new Class object that
  inherits the properties of the original Class, while adding others. This isn't properly part of this assignment, but it's worth thinking
  about how to extend what you're practicing here in useful ways.*

The `Deck` should create the instances of `Card` in its constructor method when it is instantiated. When you have a real-world
deck of cards, there's an associated order of those cards, and your implementation should also have this characteristic. Is
there a built-in data structure in Python that would naturally give the `Card` objects in your `Deck` object this ordering property?

`Deck` has 2 other methods: `shuffle()` and `deal() -> Card`.
The `shuffle()` method does what it says on the tin. You may want to use the [`random.shuffle()` method from the Python 
standard library](https://docs.python.org/3.9/library/random.html#random.shuffle). The `deal() -> Card` method should
return the next card from the deck and remove it from the deck. 
For example, after a call to shuffle, the first card may be "Q of Diamonds". When `deal()` is called, it should return that
`Card` to the caller and remove it from the deck. At that point the deck would only have 51 cards left --- again, as illustrated
in the associated tests. Again, think about a function or method that Python might provide which would very naturally
accomplish this.

If you want more of a challenge, consider using the deck you have made to create a Blackjack simulator. 
This is not required for the assignment, but would be a natural extension and an opportunity to learn and practice.

What other classes would a Blackjack simulator need?
See https://en.wikipedia.org/wiki/Blackjack for more information on Blackjack.
