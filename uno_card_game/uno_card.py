from termcolor import colored


class UnoCard:
    def __init__(self, type: str, color: str):
        self.type = type
        self.color = color

    def __str__(self):
        format = f"[ {self.type}]" if self.type in range(10) else f"[{self.type}]"
        return colored(format, self.color, attrs=["reverse", "blink"])
