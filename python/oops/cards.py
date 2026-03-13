""" python object- oriented programming (OOP) """

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

if __name__ =="__main__":
    card1 = Card("Ace", "Hearts")
    card2 = Card("King", "Spades")
    card3 = Card("Jack", "Clubs")
    card4 = Card("Three", "Diamonds")
    
    print(card1)
    print(card2)
    print(card3)
    print(card4)