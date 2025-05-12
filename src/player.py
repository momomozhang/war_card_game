"""
Player module for the War Card Game.

This module defines Player class. It represents a player's collection of cards during the game.
"""

import random
from card import Card

class Player:
    """A player's hand of cards during the war game."""

    def __init__(self, name, cards=None):
        """
        Initialize a player's hand with name and cards.

        Args:
            name (str): output from main.py
            cards (list, optional): a list of card object, default to None
        """
        self.name = name
        # If no cards provided, create empty hand
        self.cards = cards if cards is not None else []

    def card_count(self):
        """
        Get the number of cards in the player's hand.

        Returns:
            int: Number of cards in the hand
        """
        return len(self.cards)
    
    def draw_card(self, num_cards):
        """
        Draw a specific number of cards from the top of the player's hand. 
        When the player has less cards than the required, return an empty list.
        Else, draw the first num_cards} amount of cards.
        Update self.cards to the current remaining cards.

        Args:
            count: number of cards to draw. 
            It should equal to 1 during normal play, equal to 4 during "war" (3 cards to put aside, 4th card to compare)
        
        Returns:
            drawn_cards: List of cards drawn, or empty list when insufficient cards
        """
        if num_cards != 1 and num_cards != 4:
            raise ValueError("Draw 1 card during normal play. Draw 4 cards during \"war\"!")

        # when a player has less card(s) than the required number, return empty list
        if len(self.cards) < num_cards:
            return []
        else:
            #draw the required number of cards
            drawn_cards = self.cards[:num_cards]
            #update the player's remaining cards
            self.cards = self.cards[num_cards:]
        return drawn_cards
    
    def add_cards(self, cards_on_table):
        """
        Add the cards on the table to the bottom of the player's hand.

        Args:
            cards_on_table: The list of Card objects, die both players have drawn from previous round(s)
        """

        # Shuffle the cards before adding the cards
        random.shuffle(cards_on_table)
        #extend the self.cards list with new shuffled cards
        self.cards.extend(cards_on_table)

    def has_cards(self):
        """
        Check if the player has any cards left.

        Returns:
            bool: True if player has cards, False otherwise
        """
        return len(self.cards) > 0

    def __str__(self):
        """String representation of the player's hand."""
        return f"{self.name} has {self.card_count()} cards."