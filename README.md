# war_card_game

Game logic:
- Ask user if they want to play
- If yes, ask input to acquire the players' names 
- create a 52-card standard deck
- first decide which player gets the 1st card, then deal the deck alternately to 2 players
- each player draw 1 card from the top of their respective deck
- whoever wins take both cards, shuffle them, then add both cards to the bottom of their deck
- in case of a draw, a "War" starts:
    - draw 4 more cards from each players' deck
    - compare their 4th card
    - whoever wins take all 10 cards, shuffle them, then add all 10 cards to the bottom of their deck
    - if still a draw, repeat the "War" process
- the player who gets 52 cards, win the game

So far done:
- define Card class
- define Deck class
- define game logic

next to work on:
- define PlayerHand class
