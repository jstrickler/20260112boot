""" Module doc"""
class Card:  # inherits from 'object' class
    def __init__(self, rank, suit): # 'self' is the instance
        self._rank = rank
        self._suit = suit

    # @deco
    # def some_function():
    #     pass
        

    @property
    def rank(self):  # getter property
        """
        rank value of card as a string (not an integer)

        :return _type_: _description_
        """
        return self._rank
    
    @rank.setter
    def rank(self, new_value):  # setter property
        if isinstance(new_value, str):
            self._rank = new_value
        else:
            wrong_type = type(new_value).__name__
            raise TypeError(f"Rank must be a string, not a {wrong_type}")

    @property
    def suit(self):  # getter property
        return self._suit
    
    @suit.setter
    def suit(self, value):
        self._suit = value

    def __str__(self): # human-friendly view of object
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):  # how to create the object
        return f'Card("{self.rank}", "{self.suit}")'

if __name__ == "__main__":
    c1 = Card("8", "Diamonds")
    print(f"{c1 = }")     # repr()
    print(f"{c1 = !s}")   # str()
    print(f"{c1.rank = }")
    c2 = Card("Ace", 'Hearts')
    print(f"{c2.suit = }")
    c2.rank = "King"
    print(f"{c2.rank = }")
    try:
        c2.rank = 10  #  calls setter property for that attribute (i.e., rank)
    except TypeError as err:
        print(err)
    else:
        print(f"{c2.rank = }")
    print("all done")
    
    
