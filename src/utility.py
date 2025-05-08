"""
Utility module for the War card game.

This module provides helper functions used across the game.
"""

import random
from card import Card
from player import Player

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
        
def get_players_names():
    """
    Inform the user now we need 2 players. Ask players enter their names.

    Return:
        A list of two player names.
    """
    player1 = input("Enter the name of Player A: ")
    player2 = input("Enter the name of Player B: ")
    player_names = [player1, player2]
    return player_names

def shuffle_cards(cards):
    """Shuffle the cards randomly"""
    random.shuffle(cards)
    return cards

def assign_hand(player_names, two_hands):
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
        1: if card1 is bigger
        2: if card2 is bigger
        0: if it's a tie
    """
    if card1.rank_value == card2.rank_value:
        print(f"Both cards have same rank. This round is a draw!")
        return 0
    elif card1.rank_value > card2.rank_value:
        print(f"{card1} wins this round!")
        return 1
    else:
        print(f"{card2} wins this round!")
        return 2

def play_round(player1, player2, num_cards=1):
    """
    Play a round of the War card game.

    Args:
        - player1_hand: player1's hand of cards
        - player2_hand: player2's hand of cards
        - num_cards: 1 when normal play, 4 in "war. Default to 1.
    Returns:
        0: continue game
        1: player1 wins
        2: if player2 wins
    """

    # Each player draws a card
    cards1 = player1.draw_card(num_cards)
    cards2 = player2.draw_card(num_cards)

    print(f"{player1.name} plays: {cards1[-1]}")
    print(f"{player2.name} plays: {cards2[-1]}")

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
        0: no winner yet
        1: player1 wins
        2: player2 wins
    """
    # check if either player has all 52 cards
    if player1.card_count() == 52:
        #print(f"\n{player1} has all 52 cards!\n {player1} wins!")
        return 1 #player1 wins
    elif player2.card_count() == 52:
        #print(f"\n{player2} has all 52 cards!\n {player2} wins!")
        return 2 #player2 wins

    # check if either player doesn't have enough cards for the next draw
    if player1.card_count() < required_cards:
        #print(f"\n{player1} doesn't have enough cards to continue.\n{player2} wins!")
        return 2 #player2 wins
    elif player2.card_count() < required_cards:
        #print(f"\n{player2} doesn't have enough cards to continue.\n{player1} wins!")
        return 1 #player1 wins

    # no winner yet
    return 0
