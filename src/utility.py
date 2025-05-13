"""
Utility module for the War card game.

This module provides helper functions used across the game.
"""

import random
import time
from card import Card
from player import Player

DRAW = 0
PLAYER1_WINS = 1
PLAYER2_WINS = 2
STANDARD_DECK_SIZE = 52

RESPONSE_PAUSE_SECONDS = 0.5
ROUND_PAUSE_SECONDS = 1
NEXT_ROUND_PAUSE_SECONDS = 1.5

def ask_play_game():
    """
    Ask the user if they want to play the game.

    Returns:
        True: if user wants to play
        False otherwise
    """
    while True:
        print("\n")
        response = input("Do you want to play War? (yes/no): ").lower()
        time.sleep(RESPONSE_PAUSE_SECONDS)
        if response.startswith("y"):
            print("\nYaaay! Let's play!")
            return True
        else:
            print("\nYou don't want to play? Sad :(")
            return False
        
def get_players_names():
    """
    Inform the user now we need 2 players. Ask players enter their names.

    Return:
        player_names: a list of two player names.
    """
    print("\n")
    player1 = input("Enter the name of Player A: ")
    time.sleep(RESPONSE_PAUSE_SECONDS)
    player2 = input("Enter the name of Player B: ")
    player_names = [player1, player2]
    return player_names

def shuffle_cards(cards):
    """Shuffle the cards randomly"""
    random.shuffle(cards)
    return cards

def distribute_hands_to_players(player_names, two_hands):
    """
    Decide which player get which hand of cards.

    Args:
        player_names: a list of both player names.
        two_hands: a nested list of two hands.

    Returns:
        the hand of cards for each player.
    """
    # shuffle the hands randomly
    random.shuffle(two_hands)

    # assign the hands of cards to players randomly
    player1_hand = two_hands[0]
    player2_hand = two_hands[1]

    return player1_hand, player2_hand

def compare_cards(card1, card2):
    """
    Compare two cards and determine the winner or if it's a draw.

    Args:
        card1: card from player1
        card2: card from player2

    Returns:
        PLAYER1_WINS: if card1 is bigger
        PLAYER2_WINS: if card2 is bigger
        DRAW: if it's a tie
    """
    if card1.rank_value == card2.rank_value:
        print(f"\nBoth cards have same rank. This round is a draw!")
        return DRAW
    elif card1.rank_value > card2.rank_value:
        print(f"\n{card1} wins this round!")
        return PLAYER1_WINS
    else:
        print(f"\n{card2} wins this round!")
        return PLAYER2_WINS

def play_round(player1, player2, cards_to_draw=1):
    """
    Play a round of the War card game.

    Args:
        - player1_hand: player1's hand of cards
        - player2_hand: player2's hand of cards
        - cards_to_draw: 1 when normal play, 4 in "war. Default to 1.
    Returns:
        DRAW: continue game
        PLAYER1_WINS: player1 wins
        PLAYER2_WINS: if player2 wins
    """

    # Each player draws a card
    cards1 = player1.draw_card(cards_to_draw)
    cards2 = player2.draw_card(cards_to_draw)

    print(f"\n{player1.name} plays: {cards1[-1]}")
    print(f"{player2.name} plays: {cards2[-1]}")
    time.sleep(ROUND_PAUSE_SECONDS)

    # compare cards
    result = compare_cards(cards1[-1], cards2[-1])

    # update table cards
    cards_to_add = cards1 + cards2

    return result, cards_to_add

def check_winner(player1, player2, required_cards=1):
    """
    Check if there's a winner based on card count.

    Args:
        player1 & player2: two player names
        required_cards: number of cards required for the next draw. 1 for normal play, 4 for "war"

    Returns:
        DRAW: no winner yet
        PLAYER1_WINS: player1 wins
        PLAYER2_WINS: player2 wins
    """
    time.sleep(ROUND_PAUSE_SECONDS)

    # check if either player has all 52 cards
    if player1.card_count() == STANDARD_DECK_SIZE:
        return PLAYER1_WINS #player1 wins
    elif player2.card_count() == STANDARD_DECK_SIZE:
        return PLAYER2_WINS #player2 wins

    # check if either player doesn't have enough cards for the next draw
    if player1.card_count() < required_cards:
        return PLAYER2_WINS #player2 wins
    elif player2.card_count() < required_cards:
        return PLAYER1_WINS #player1 wins

    # no winner yet
    return DRAW
