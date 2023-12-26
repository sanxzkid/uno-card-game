from uno_card import UnoCard
import random

class UnoDeck:    
    def __init__(self):
        self._deck = []
        self._numbers = range(10)
        self._colors = ["red", "blue", "yellow", "green"]
        self._actions = ["skip", "revert", "addTwo"]
        self._wilds = ["chooseColor", "addFourAndChooseColor"]
    
    def start(self):
        for c in self._colors:
            for n in self._numbers:
                self._deck.append(UnoCard(n, c))
            for a in self._actions:
                self._deck.append(UnoCard(a, c))
        for w in self._wilds:
            for n in range(4):
                self._deck.append(UnoCard(w, None))
        random.shuffle(self._deck)
        return self._deck