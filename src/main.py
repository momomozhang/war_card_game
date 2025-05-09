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
    time.sleep(1)
    player_names = get_players_names()

    # create, shuffle, and split a deck
    deck = Deck()
    deck.shuffle_deck()
    two_hands = deck.split_deck()

    #assign hands to players
    player1_cards, player2_cards = assign_hand(player_names, two_hands)

    # create player object
    player1 = Player(player_names[0], player1_cards)
    player2 = Player(player_names[1], player2_cards)

    # print player names and start the game
    print(f"\nWe have {player1.name} and {player2.name}!")
    print("\nLet's start the game!")
    time.sleep(2)  # Pause for 2 seconds

    # main game loop
    round = 1
    war_on = False
    table_cards = []

    while True:
        print(f"\n-----Round {round}-----")
        #print("\n")
        print(str(player1))
        print(str(player2))

        # check for winner before starting a new round 
        winner_check = check_winner(player1, player2, 4 if war_on else 1)
        if winner_check == 1:
            print(f"\n{player1.name} has won the game!")
            if war_on and len(player2.cards()) < 4:
                print(f"\nBecause {player2.name} doesn't have enough cards to start a War!")
            break
        elif winner_check == 2:
            print(f"\n{player2.name} has won the game!")
            if war_on and len(player1.cards()) < 4:
                print(f"\nBecause {player1.name} doesn't have enough cards to start a War!")
            break
        else:
            pass

        # reset war flag if we start a new round
        if not war_on:
            table_cards = []

        # play a round
        if war_on:
            result, cards_to_add = play_round(player1, player2, 4)
            table_cards += cards_to_add

            time.sleep(2)

            if result == 1:
                print(f"\n{player1.name} wins the War and takes all the cards on the table!")
                player1.add_cards(table_cards)
                war_on = False
            elif result == 2:
                print(f"\n{player2.name} wins the War and takes all the cards on the table!")
                player2.add_cards(table_cards)
                war_on = False
            elif result == 0:
                print("\nIt's a draw. Another War!")
                war_on = True
            else:
                raise ValueError("\nWar result went wrong.")
        
        if not war_on:
            result, cards_to_add = play_round(player1, player2, 1)
            table_cards += cards_to_add

            time.sleep(2)

            if result == 1:
                print(f"\n{player1.name} wins this round and takes all the cards on the table!")
                player1.add_cards(table_cards)
            elif result == 2:
                print(f"\n{player2.name} wins this round and takes all the cards on the table!")
                player2.add_cards(table_cards)
            elif result == 0:
                print("\nIt's a draw! War is on!")
                war_on = True
            else:
                raise ValueError("\nRound result went wrong.")
        
        # slow down the game to make it a bit less mechanical
        time.sleep(1)
        print("\nMoving to next round in 3 seconds...")
        time.sleep(3)  # Pause for 3 seconds

        # increment the round count
        round += 1

if __name__ == "__main__":
    main()