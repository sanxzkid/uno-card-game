from unittest.mock import patch, MagicMock

import pytest

from uno_card_game.uno_card import UnoCard
from uno_card_game.uno_deck import UnoDeck
from uno_card_game.uno_game import UnoGame


# Test initialization of the UnoGame
def test_init():
    game = UnoGame(hand_size=7, players_size=4)
    assert game.initial_hand_size == 7
    assert game.orientation == "CW"
    assert game.show_option == "row-options"
    assert game.error == ""
    assert isinstance(game.uno_deck, UnoDeck)
    assert len(game.players) == 4
    assert game.player_idx == 0
    assert isinstance(game.top_card, UnoCard)


# Test the create_players method
def test_create_players():
    game = UnoGame(hand_size=7, players_size=4)
    players = game.create_players(4)
    assert len(players) == 4
    for player in players:
        assert len(player.hand) == 7


# Test the change_color method with mocking input
@patch('builtins.input', side_effect=['1'])
def test_change_color(mock_input):
    game = UnoGame(hand_size=7, players_size=4)
    game.top_card = UnoCard('wild', '+4')
    game.change_color()
    assert game.top_card.color == game.uno_deck.deck_colors[0].color


# Test the buy method
def test_buy():
    game = UnoGame(hand_size=7, players_size=4)
    initial_deck_size = len(game.deck)
    game.buy(1)
    assert len(game.player_hand) == 1
    assert len(game.deck) == initial_deck_size - 1


# Test the restore_dead_deck method
def test_restore_dead_deck():
    game = UnoGame(hand_size=7, players_size=4)
    game.dead_deck = [UnoCard('red', '1'), UnoCard('blue', '2')]
    game.restore_dead_deck()
    assert len(game.deck) == 2
    assert len(game.dead_deck) == 0


# Test the invert method
def test_invert():
    game = UnoGame(hand_size=7, players_size=4)
    assert game.orientation == "CW"
    game.invert()
    assert game.orientation == "CCW"
    game.invert()
    assert game.orientation == "CW"


# Test the next_player method
def test_next_player():
    game = UnoGame(hand_size=7, players_size=4)
    assert game.player_idx == 0
    game.next_player()
    assert game.player_idx == 1
    # Test wrapping around to the first player
    game.player_idx = len(game.players) - 1
    game.next_player()
    assert game.player_idx == 0
    # Test counter-clockwise orientation
    game.orientation = "CCW"
    game.next_player()
    assert game.player_idx == len(game.players) - 1


# Test the refresh_screen method with mocking os.system
@patch('os.system', MagicMock())
def test_refresh_screen():
    game = UnoGame(hand_size=7, players_size=4)
    game.refresh_screen()
    # Assertions can be made about the expected state after refreshing the screen
    # However, since this method primarily prints to the console and clears the screen,
    # there may not be much to assert on without capturing stdout.


# Test the waiting_screen method with mocking os.system and input
@patch('os.system', MagicMock())
@patch('builtins.input', MagicMock())
def test_waiting_screen():
    game = UnoGame(hand_size=7, players_size=4)
    game.waiting_screen()
    # Similar to refresh_screen, this method's main actions are to clear the screen and wait for input,
    # so assertions would be limited.


# Test the show_header method
def test_show_header(capsys):
    game = UnoGame(hand_size=7, players_size=4)
    game.show_header()
    captured = capsys.readouterr()
    assert "Uno Card Game" in captured.out


# Test the show_error method
def test_show_error(capsys):
    game = UnoGame(hand_size=7, players_size=4)
    game.error = "Test Error"
    game.show_error()
    captured = capsys.readouterr()
    assert "Test Error" in captured.out
    assert game.error == ""


# Test the show_cards method
def test_show_cards(capsys):
    game = UnoGame(hand_size=7, players_size=4)
    cards = [UnoCard('red', '1'), UnoCard('blue', '2')]
    game.show_cards("Test Cards", cards)
    captured = capsys.readouterr()
    assert "(1)[red]" in captured.out
    assert "(2)[blue]" in captured.out


# Run the tests
if __name__ == "__main__":
    pytest.main()
