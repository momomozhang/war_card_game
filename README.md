# War Card Game

A terminal-based implementation of the classic card game "War" I built while learning Python & Git/Github.

## Game Rules

I've implemented the classic War card game with these rules:
* Each player gets half of a standard 52-card deck
* On each turn, both players flip their top card
* Highest card wins (2 is lowest, Ace is highest)
* Winner takes both cards and puts them at the bottom of their deck
* If there's a tie, it triggers a "War":
   * Both players place 3 cards face down
   * They flip a 4th card, highest card wins all 10 cards
   * If there's another tie, the War continues
* Game ends when someone collects all 52 cards
* If a player doesn't have enough cards for a War, they lose

## Project Structure

```
war_card_game/
├── __init__.py
├── card.py        # Defines a playing card
├── deck.py        # Handles creating and splitting the deck
├── player.py      # Manages each player's cards and actions
├── utility.py     # Contains game helper functions
└── main.py        # Runs the main game loop
```

## What I Learned

### Python Skills:
* Creating classes, objects, and functions
* Writing modular code
* Adding proper error handling
* Using dunder methods like __str__
* Writing good docstrings

### Git & GitHub Experience:
* Making commits
* Using tags for version tracking
* Pushing code to remote repos
* Managing project files

## Key Takeaways

1. **Plan Before Coding**: With tools like GitHub Copilot and Claude AI around, I realized I need to be my own product manager. Sketching out the project and specifications before writing any code is vital.

2. **Module Organization Matters**: Breaking the code into logical files made everything easier to manage. I don't want to think about debugging this if it was all in one file!

3. **Document Everything**: Future-me will thank present-me for all those comments and docstrings.

4. **Design Classes Carefully**: Spending time thinking about how the Card, Deck, and Player classes should work together paid off. The game logic flows naturally.

## What's Next

In an ideal world, below features could be added:
* Unittests
* Proper web-based interface
* Save/load game feature
* Game statistics (longest war, quickest win, etc.)
* Current game rules require no player strategy. It's purely random. To make it fun for the user, could modify the game rules to allow user strategies.
* AI / Computer opponent

However, I won't have time to continue this project. I'm moving to the next stage: building a real life relevant application using AWS services!

## Skills To Build

* **Product Thinking**: Get better at planning features and project specs
* **Clean Code**: Keep studying best practices for readable, maintainable code
* **Testing**: Learn how to write proper unit tests
* **UI Design**: Explore basic UI principles even for simple projects

## How to Run the Game

1. Clone this repo:
```bash
git clone https://github.com/yourusername/war_card_game.git
cd war_card_game
```

2. Run the game:
```bash
python main.py
```

3. Follow the prompts and enjoy!

## Want to Help?

Feel free to fork the repo and make improvements. Just submit a PR with your changes.

---

Made with ☕ and Python
