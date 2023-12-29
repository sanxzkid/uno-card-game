from uno_player import UnoPlayer
from uno_deck import UnoDeck
from uno_card import UnoCard
import os


class UnoGame:
    def __init__(self, hand_size: int, players_size: int):
        self.initial_hand_size = hand_size
        self.orientation = "CW"
        self.show_option = "row-options"
        self.error = ""
        self.uno_deck = UnoDeck()
        self.uno_deck.shuffle()
        self.deck: list[UnoCard] = self.uno_deck.deck
        self.dead_deck: list[UnoCard] = []
        self.players = self.create_players(players_size)
        self.player_idx = 0
        self.player_hand: list[UnoCard] = []
        self.top_card = self.deck.pop(0)
        
    def start(self):
        while True:
            self.refresh_screen()
            
            self.show_error()
            selected_card = self.select_card()
            
            if selected_card == "P":
                self.next_player()
            elif len(self.deck) > 0 and selected_card == "B":
                self.buy(1)
            elif selected_card == "S":
                self.player_hand.sort(key=lambda card: str(card))
            elif not selected_card.isdigit():
                self.error = "Invalid Option, only digits"
            elif int(selected_card) not in range(1, len(self.player_hand) + 1):
                self.error = f"Invalid Option, out of range [1] to [{len(self.player_hand)}]"
            elif self.player_hand[int(selected_card) - 1].color != None and self.player_hand[int(selected_card) - 1].type != self.top_card.type and self.player_hand[int(selected_card) - 1].color != self.top_card.color:
                self.error = "Invalid Card, should have same color or same type"
            else:
                self.play_card(selected_card)
                
                if len(self.player_hand) == 0:
                    print("WINNER")
                    return 
                
                if self.top_card.color == None:
                    self.change_color()
                if self.top_card.type == "🔄":
                    self.invert()
                    
                self.next_player()
                
                if self.top_card.type == "+4":
                    self.buy(4)
                elif self.top_card.type == "+2":
                    self.buy(2)
                elif self.top_card.type == "❌":
                    self.next_player()
                    
                self.waiting_screen()

    def select_card(self):
        action_message = ""
        if len(self.deck) > 0:
            action_message = "Buy (B) | Pass (P) | Sort (S) | Choose one card: "
        else:
            action_message = "Pass (P) | Sort (S) | Choose one card: "
            if len(self.dead_deck) > 10:
                self.restore_dead_deck()
        selected_card = input(action_message).upper()
        return selected_card

    def play_card(self, selected_card: str):
        print(self.player_hand[int(selected_card) - 1])
        self.dead_deck.append(self.top_card)
        self.top_card = self.player_hand.pop(int(selected_card) - 1)
        
    def create_players(self, quantity: int):
        players = []
        for i in range(0, quantity):
            players.append(UnoPlayer(f"Player { i + 1 }", 0, self.deck[0: self.initial_hand_size]))
            del self.deck[0: self.initial_hand_size]
        return players

    def change_color(self):
        while True:
            self.refresh_screen()
            self.show_cards("Colors", self.uno_deck.deck_colors)
            self.show_error()
            selected_color = input("Choose one color: ")
            if not selected_color.isdigit():
                self.error = "Invalid Option, only digits"
            elif int(selected_color) not in range(1, 5):
                self.error = "Invalid Option, out of range [1] to [4]"
            else:
                self.top_card.color = self.uno_deck.deck_colors[int(selected_color) - 1].color
                break

    def buy(self, quantity: int):
        for i in range(quantity):
            self.player_hand.append(self.deck.pop(0))

    def restore_dead_deck(self):
        self.deck = self.dead_deck
        self.uno_deck.shuffle()

    def invert(self):
        if self.orientation == "CW":
            self.orientation = "CCW"
        elif self.orientation =="CCW":
            self.orientation = "CW"

    def next_player(self):
        if self.orientation == "CW":
            if self.player_idx < len(self.players) - 1:
                self.player_idx += 1
            else:
                self.player_idx = 0
        if self.orientation == "CCW":
            if self.player_idx == 0:
                self.player_idx = len(self.players) - 1
            else:
                self.player_idx -= 1
         
    def refresh_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.show_header()
        # self.show_cards(f"Deck cards", self.deck)
        print(f"\nTop Card\n{self.top_card}")
        self.player_hand = self.players[self.player_idx].hand
        self.show_cards(f"Player {self.player_idx + 1} cards", self.player_hand)
        
    def waiting_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.show_header()
        print(f"\nTop Card\n{self.top_card}")
        input("Waiting next player ...")
               
    def show_header(self):
        print("------------- Uno Card Game - by sanxzkid -------------")

    def show_error(self):
        print(f"\n{self.error}")
        self.error = ""

    def show_cards(self, title: str, cards: str):
        print(f"\n{title}")
        if self.show_option == "row":
            print(" ".join([str(c) for c in cards]))
        elif self.show_option == "row-options":
            print(" ".join([f"({i + 1}){str(c)}" for i, c in enumerate(cards)]))
        elif self.show_option == "col":
            [print(c) for c in cards]
        elif self.show_option == "col-options":
            [print(f"({i + 1}){str(c)}") for i, c in enumerate(cards)]