from uno_player import UnoPlayer
from uno_deck import UnoDeck
from termcolor import colored


class UnoGame:
    def __init__(self):
        self.deck = UnoDeck().shuffle()
        print("\nShuffle Deck")
        [print(c) for c in self.deck]

        self.orientation = "CW"

        self.player1 = UnoPlayer("Player 1", 0, self.deck[0:8])
        print("\Hand Player 1")
        [print(c) for c in self.player1.hand]
        
        self.player2 = UnoPlayer("Player 2", 0, self.deck[8:15])
        print("\Hand Player 2")
        [print(c) for c in self.player2.hand]

        del self.deck[0:15]
