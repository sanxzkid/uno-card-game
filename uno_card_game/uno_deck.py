from uno_card_game.uno_card import UnoCard
import random


class UnoDeck:
    def __init__(self):
        self.deck: list[UnoCard] = []

        numbers = range(10)
        colors = ["red", "cyan", "yellow", "green"]
        actions = ["❌", "🔄", "+2"]
        wilds = ["🎨", "+4"]
        
        self.deck_colors = [UnoCard(" ", colors[i]) for i in range(4)]

        for c in colors:
            for n in numbers:
                self.deck.append(UnoCard(str(n), c))
            for a in actions:
                self.deck.append(UnoCard(a, c))
        for w in wilds:
            for n in range(4):
                self.deck.append(UnoCard(w, "white"))

    def shuffle(self):
        random.shuffle(self.deck)
