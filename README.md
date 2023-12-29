# Uno Card Game

This repository contains the implementation of a text-based Uno card game. The game is played in the console and supports multiple players.

## Class UnoGame

The `UnoGame` class represents a game of Uno with all the necessary attributes and methods to play the game.

### Attributes

- `initial_hand_size` (int): The number of cards each player starts with.
- `orientation` (str): The direction of play, either "CW" for clockwise or "CCW" for counterclockwise.
- `show_option` (str): The display format for the cards, options include "row", "row-options", "col", "col-options".
- `error` (str): Error message to display to the user.
- `uno_deck` (UnoDeck): The UnoDeck object representing the main deck of Uno cards.
- `deck` (list[UnoCard]): The main deck of Uno cards.
- `dead_deck` (list[UnoCard]): The pile of played cards.
- `players` (list[UnoPlayer]): The list of players in the game.
- `player_idx` (int): The index of the current player.
- `player_hand` (list[UnoCard]): The hand of the current player.
- `top_card` (UnoCard): The top card on the play pile.

### Methods

- `start()`: Begins the Uno game loop, handling turns and game flow.
- `select_card()`: Prompts the current player to select a card to play, buy, pass, or sort their hand.
- `play_card(selected_card: str)`: Plays the selected card from the current player's hand onto the play pile.
- `create_players(quantity: int)`: Creates the specified number of UnoPlayer objects and deals the initial hands.
- `change_color()`: Allows the current player to change the color of play after playing a wild card.
- `buy(quantity: int)`: Adds the specified number of cards to the current player's hand from the deck.
- `restore_dead_deck()`: Restores the main deck from the dead deck when the main deck runs out of cards.
- `invert()`: Inverts the direction of play.
- `next_player()`: Advances the game to the next player in the current direction of play.
- `refresh_screen()`: Clears the console and displays the current game state.
- `waiting_screen()`: Displays a waiting screen for the next player to take their turn.
- `show_header()`: Displays the game header.
- `show_error()`: Displays the current error message, if any.
- `show_cards(title: str, cards: list[UnoCard])`: Displays the cards with the specified title and format based on the `show_option` attribute.

## Getting Started

To play the Uno card game, clone the repository and run the main script:

```bash
git clone https://github.com/your-username/uno-card-game.git
cd uno-card-game
poetry install
poetry shell
python uno-card-game
```
