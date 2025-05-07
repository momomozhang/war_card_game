"""
PlayerHand module for the War Card Game.

This module defines PlayerHand class. It represents a player's collection of cards during the game.
"""

from card import Card
from utility import shuffle_cards

class PlayerHand:
    """A player's hand of cards during the war game."""

    def __init__(self, player_name, cards=None):
        """
        Initialize a player's hand with name and cards.

        Args:
            player_name (str): output from main.py
            cards (list, optional): a list of card object, default to None
        """
        self.player_name = player_name
        self.cards = cards if cards is not None else []

    def card_count(self):
        """
        Get the number of cards in the player's hand.

        Returns:
            int: Number of cards in the hand
        """
        return len(self.cards)
    
    def draw_card(self, count):
        """
        Draw a specific number of cards from the top of the player's hand.

        Args:
            count: number of cards to draw. 
            It should equal to 1 during normal play, equal to 4 during "war" (3 cards to put aside, 4th card to compare)
        
        Returns:
            When the player has less cards than the required, return an empty list.
            Else, draw the first {count} amount of cards.
            Update self.cards to the current remaining cards.
        """
        if count != 1 and count != 4:
            raise ValueError("Draw 1 card during normal play. Draw 4 cards during \"war\"!")

        # when a player has less card(s) than the required number, return empty list
        if len(self.cards) < count:
            return []
        else:
            #draw the required number of cards
            drawn_cards = self.cards[:count]
            #update the player's remaining cards
            self.cards = self.cards[count:]
        return drawn_cards
    
    def add_cards(self, new_cards):
        """
        Add new cards to the bottom of the player's hand.

        Args:
            new_cards: a list of Card objects to add. 
        """
        #check if the number of cards is correct
        if len(new_cards) != 2 and len(new_cards) != 10:
            raise ValueError("Number of new cards not correct.\nDuring normal rounds there should be 2 cards.\nDuring "war" there should be 10 cards.")


        # Shuffle the cards before adding the cards
        shuffled_new_cards = shuffle_cards(new_cards)
        #extend the self.cards list with new shuffled cards
        self.cards.extend(shuffled_new_cards)

def has_cards(self):
    """
    Check if the player has any cards left.

    Returns:
        bool: True if player has cards, False otherwise
    """
    return len(self.cards) > 0

def __str__(self):
    """String representation of the player's hand."""
    return f"{self.player_name}'s hand has {self.card_count()} cards."