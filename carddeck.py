import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._discards = []
        self._make_deck()

    def _make_deck(self):
        self._cards = []  # holds the cards for this deck
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def discard(self, card):
        self._discards.append(card)

    def reset_deck(self):
        self._cards.extend(self._discards)
        self._discards.clear()  # empty the list

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards
    
    @property
    def discards(self):
        return self._discards
    
    def peek_discard(self):
        return self._discards[-1]
    
    def __add__(self, other):  # implement "+" operator
        new_deck = CardDeck()
        new_deck._cards = self.cards + other.cards
        return new_deck

    # add __str__() and __repr__()
    
if __name__ == "__main__":
    d1 = CardDeck()  # 
    d2 = CardDeck()  #
    d1.shuffle()
    d2.shuffle()
    print(f"{d1 = }")
    print(f"{d1.cards = }")
    for i in range(5):
        card = d1.draw()
        d1.discard(card)
        print(f"{card = }")

    print(f"{d1.discards = }")
    print(f"{d1.peek_discard() = }")
    print(f"{len(d1.cards) = }")
    print(f"{len(d1.discards) = }")
    print(f"{len(d2.cards) = }")
    print(f"{len(d2.discards) = }")
    
    d1.reset_deck()
    print(f"{len(d1.cards) = }")
    print(f"{len(d1.discards) = }")

    deck1 = CardDeck()
    deck2 = CardDeck()
    bigdeck = deck1 + deck2
    print(f"{len(bigdeck.cards) = }")
    print(f"{len(bigdeck.discards) = }")
