"""
Card module for the War card game.

This module defines the Card class, which represents a single playing card
with a suit and rank.
"""

class Card:
    """A playing card with suits and ranks."""

    # define valid suits and ranks
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    #creating numeric rank value
    rank_values = dict(zip(RANKS, range(2, 15)))

    def __init__(self, suit, rank):
        """
        initialize a card with suit and rank

        raises:
            ValueError: if suit or rank is invalid
        """

        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit {suit}. Must be one of {Card.SUITS}")
        
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank {rank}. Must be one of {Card.RANKS}")
        
        self.suit = suit
        self.rank = rank
        self.rank_value = Card.rank_values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.suit}', '{self.rank}')"
    