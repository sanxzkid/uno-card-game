from uno_card import UnoCard
import random


class UnoDeck:
    def __init__(self):
        self.deck = []

        numbers = range(10)
        colors = ["red", "blue", "yellow", "green"]
        actions = ["skip", "revert", "addTwo"]
        wilds = ["chooseColor", "addFourAndChooseColor"]

        for c in colors:
            for n in numbers:
                self.deck.append(UnoCard(n, c))
            for a in actions:
                self.deck.append(UnoCard(a, c))
        for w in wilds:
            for n in range(4):
                self.deck.append(UnoCard(w, None))

        for c in self.deck:
            print(c)

    def shuffle(self):
        shuffled_deck = self.deck.copy()
        random.shuffle(shuffled_deck)
        return shuffled_deck
