"""
    hand.py
    creating the hand class
"""

CARD_VALUE = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
              "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
              "Q": 10, "K": 10, "A": 11}


class Hand:
    """ class: Hand
        Attributes: cards, value
        Methods: add_card (appends a new card to cards)
                 calc_value (calculates the value of the hand)
    """

    def __init__(self, cards=[], value=0):
        """
            Constructor -- creates a new instance of a hand
            Parameters: self -- the current object
                        cards -- a list of cards in the hand
                        value -- value of the hand
        """

        self.cards = cards
        self.value = value

    def add_card(self, card):
        self.cards.append(card)

    def calc_value(self):
        """
        calculates the value of the current hand and updates the
        value of the hand
        :return: None
        """
        value = 0

        non_aces = [card for card in self.cards if card != 'A']
        aces = [card for card in self.cards if card == 'A']

        for card in non_aces:
            value += CARD_VALUE[card]

        count = 0
        for card in aces:
            value += 1
            count += 1
            if value <= 11 and len(aces) == count:
                value += 10


        self.value = value

    def get_value(self):
        """
        returns the value of the current hand
        """
        return self.value

    def __str__(self):
        """
        returns a string describing the state of the current hand
        """
        hand = ""
        for card in self.cards:
            hand += (card + " ")
        return  f"Current player's hand is {hand}with a value of {self.value}"
