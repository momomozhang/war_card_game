"""
Utility module for the War card game.

This module provides helper functions used across the game.
"""

import random
from card import Card

def ask_play_game():
    """
    Ask the user if they want to play the game.

    Returns:
        True: if user wants to play
        False otherwise
    """
    while True:
        response = input("Do you want to play War? (yes/no): ").lower()
        if response.startswith("y"):
            print("Yaaay! Let's play!")
            return True
        else:
            print("You don't want to play? Sad :(")
            return False
        
def get_players_name():
    """
    Inform the user now we need 2 players. Ask players enter their names.

    Return:
        A list of two player names.
    """
    player_a = input("Enter the name of Player A: ")
    player_b = input("Enter the name of Player B: ")
    players = [player_a, player_b]
    return players

def assign_hand_to_player(players, two_hands):
    """
    Decide which player get which hand of cards.

    Args:
        - A list of both player's names.
        - A list of both hands of cards.

    Returns:
        the hand of cards for each player.
    """
    # shuffle the hands randomly
    random.shuffle(two_hands)

    # assign the hands of cards to players randomly
    player_a_hand = two_hands[0]
    player_b_hand = two_hands[1]

    return player_a_hand, player_b_hand

def compare_cards(card1, card2):
    """
    Compare two cards and determine the winner or if it's a draw.

    Args:
        card1: card from player1
        card2: card from player2

    Returns:
        1: if card1 is bigger
        2: if card2 is bigger
        0: if it's a tie
    """
    if card1.rank_value == card2.rank_value:
        return 0
    elif card1.rank_value > card2.rank_value:
        return 1
    else:
        return 2
    
def shuffle_cards(cards):
    """Shuffle the cards randomly"""
    random.shuffle(cards)
    return cards