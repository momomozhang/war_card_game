"""
Card module for the War card game.

This module defines the Card class, which represents a single playing card
with a suit and rank.
"""

class Card:
    """A playing card with suits and ranks."""

    # Define valid suits and ranks
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    # Creating numeric rank value
    RANK_TO_VALUE_MAP = dict(zip(RANKS, range(2, 15)))

    def __init__(self, suit, rank):
        """
        Initialize a card with suit and rank

        Args:
            suit(str): the suit of the card
            rank(str): the rank of the card

        Raises:
            ValueError: if suit or rank is invalid
        """

        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit {suit}. Must be one of {Card.SUITS}")
        
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank {rank}. Must be one of {Card.RANKS}")
        
        self.suit = suit
        self.rank = rank
        self.rank_value = Card.RANK_TO_VALUE_MAP[rank]

    def __str__(self):
        """Return a string representation of the card."""
        return f"{self.rank} of {self.suit}"

    