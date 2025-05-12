"""
Main module for the War card game.

It implements the core game loop.
"""

from card import Card
from deck import Deck
from player import Player 
from utility import *
import time 

def main():
    """Main function to run the War card game."""

    # ask if user wants to play
    if not ask_play_game():
        return

    # get player names
    time.sleep(RESPONSE_PAUSE_SECONDS )
    player_names = get_players_names()

    # create, shuffle, and split a deck
    deck = Deck()
    deck.shuffle()
    two_hands = deck.split_in_half()

    #assign hands to players
    player1_cards, player2_cards = distribute_hands_to_players(player_names, two_hands)

    # create player object
    player1 = Player(player_names[0], player1_cards)
    player2 = Player(player_names[1], player2_cards)

    # print player names and start the game
    print(f"\nWe have {player1.name} and {player2.name}!")
    print("\nLet's start the game!")
    time.sleep(2)  # Pause for 2 seconds

    # main game loop
    current_round = 1
    is_war = False
    cards_on_table = []

    while True:
        print(f"\n-----Round {current_round}-----")
        #print("\n")
        print(str(player1))
        print(str(player2))

        # check for winner before starting a new round 
        winner_check = check_winner(player1, player2, 4 if is_war else 1)
        if winner_check == PLAYER1_WINS:
            print(f"\n{player1.name} has won the game!")
            if is_war and len(player2.cards()) < 4:
                print(f"\nBecause {player2.name} doesn't have enough cards to start a War!")
            break
        elif winner_check == PLAYER2_WINS:
            print(f"\n{player2.name} has won the game!")
            if is_war and len(player1.cards()) < 4:
                print(f"\nBecause {player1.name} doesn't have enough cards to start a War!")
            break
        else:
            pass

        # reset war flag if we start a new round
        if not is_war:
            cards_on_table = []

        # play a round
        if is_war:
            result, cards_to_add = play_round(player1, player2, 4)
            cards_on_table += cards_to_add

            time.sleep(ROUND_PAUSE_SECONDS)

            if result == PLAYER1_WINS:
                print(f"\n{player1.name} wins the War and takes all {len(cards_on_table)} cards on the table!")
                player1.add_cards(cards_on_table)
                is_war = False
            elif result == PLAYER2_WINS:
                print(f"\n{player2.name} wins the War and takes all {len(cards_on_table)} cards on the table!")
                player2.add_cards(cards_on_table)
                is_war = False
            elif result == DRAW:
                print("\nIt's a draw. Another War!")
                is_war = True
            else:
                raise ValueError("\nWar result went wrong.")
        
        elif not is_war:
            result, cards_to_add = play_round(player1, player2, 1)
            cards_on_table += cards_to_add

            time.sleep(ROUND_PAUSE_SECONDS)

            if result == PLAYER1_WINS:
                print(f"\n{player1.name} wins this round and takes all {len(cards_on_table)} cards on the table!")
                player1.add_cards(cards_on_table)
            elif result == PLAYER2_WINS:
                print(f"\n{player2.name} wins this round and takes all {len(cards_on_table)} cards on the table!")
                player2.add_cards(cards_on_table)
            elif result == DRAW:
                print("\nIt's a draw! War is on!")
                is_war = True
            else:
                raise ValueError("\nRound result went wrong.")
        
        # slow down the game to make it a bit less mechanical
        time.sleep(RESPONSE_PAUSE_SECONDS )
        print("\nMoving to next round in 3 seconds...")
        time.sleep(NEXT_ROUND_PAUSE_SECONDS)  # Pause for 3 seconds

        # increment the round count
        current_round += 1

if __name__ == "__main__":
    main()