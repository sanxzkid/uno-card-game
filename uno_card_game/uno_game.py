from uno_deck import UnoDeck


class UnoGame:
    def __init__(self):
        self.deck = UnoDeck().shuffle()
        self.players = []
