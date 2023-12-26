class UnoCard:
    def __init__(self, type, color):
        self.type = type
        self.color = color
    def __str__(self):
        return f"{self.type, self.color}"