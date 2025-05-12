"""
Deck module for the War card game.

This module defines the Deck class. It represents a standard 52 card deck.
"""

import random
from card import Card

class Deck:
    """Define 1) standard 52-card deck 2) the split_card method"""

    STANDARD_DECK_SIZE = 52
    NUMBER_OF_PLAYERS = 2

    def __init__(self):
        """Create a deck with 52 cards"""
        self.cards = [] #create an empty card list

        #loop throught SUITS and RANKS to append each card to the list
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """Shuffle the deck randomly."""
        random.shuffle(self.cards)

    def split_in_half(self):
        """
        Split the deck by dealing cards alternately to two players.
        
        Returns:
            2 lists each containing 26 cards for each player.

        Raises:
            ValueError: when the deck doesn't have exactly 52 cards.
        """
        if len(self.cards) != self.STANDARD_DECK_SIZE:
            raise ValueError("Deck must have exactly {self.STANDARD_DECK_SIZE} cards to split!")
        
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
        