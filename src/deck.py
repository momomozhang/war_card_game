"""
Deck module for the War card game.

This module defines the Deck class. It represents a standard 52 card deck and provides methods for shuffling cards.
"""

import random
from card import Card

class Deck:
    """Define 1) standard 52-card deck 2) the shuffle & split_card & deal_card method"""

    def __init__(self):
        """Create a deck with 52 cards"""
        self.cards = [] #create an empty card list

        #loop throught SUITS and RANKS to append each card to the list
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))


    def split_deck(self):
        """
        Split the deck by dealing cards alternately to two players.
        
        Returns:
            2 lists each containing 26 cards for each player.

        Raises:
            ValueError: when the deck doesn't have exactly 52 cards.
        """
        if len(self.cards) != 52:
            raise ValueError("Deck must have exactly 52 cards to split!")
        
        #Create empty list for each player's cards
        hand1 = []
        hand2 = []

        #Assign the cards to each player alternately
        for index, card in enumerate(self.cards):
            if index % 2 == 0:
                hand1.append(card)
            else:
                hand2.append(card)

        two_hands = [hand1, hand2]
        return two_hands
        