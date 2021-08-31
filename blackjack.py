import random
from random import choice


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.suit} of {self.value}"


class Deck:
    def __init__(self,):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"]
                      for v in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, player):
        single_card = self.cards.pop()
        player.cards.append(single_card)
        return single_card


class Player:

    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self, busted=False):
        self.value = 0
        for card in self.cards:
            self.value += int(card.value)
            if self.value > 21:
                busted = True
                return busted

    def get_value(self):
        self.calculate_value
        return self.value

    def display_cards(self):
        pass

    def set_play(self, player, choice):
        if choice == 'hit':
            deck.deal_card(player)
            player.play = "Hit"
        elif choice == 'stay':
            player.play = "Stay"


class Dealer(Player):

    def __init__(self):
        super().__init__()

    def display_cards(self, showall=False):
          print(self.cards)
           for card in self.cards[:1]:
                print(card)
            self.calculate_value()


class Human(Player):

    def __init__(self, name):
        self.name = name
        super().__init__()

    def display_cards(self):
        print('\n' f"{self.name} hand after dealing card:")
        print(self.cards)
        for card in self.cards:
            print(card)
            self.calculate_value()


class Game:
    def __init__(self):
        self.playing = True

    def check_for_bust(self, player):
        if player.value > 21:
            print(f"{player.name} BUST! {player.value}")
            return True

# This will Show Who Has won the game

    def compare(self, player1, player2):
        if player1.value:
            print(
                f"You busted! Dealer wins! Your score is {player1.value} ; Dealer's total is {player2.value}")
        elif player2.value:
            print(f"You win, Dealer Busted! Your total is {player1.value}")
        elif player1.value == player2.value:
            print("It is a tie. You both had the same number!")
        elif player1.value > player2.value:
            print("You win!")
        elif player1.value < player2.value:
            print("You lose")



game = Game()

player_name = input("What is your name?  ")

while game.playing:

    player1 = Human(player_name)
    player2 = Dealer()

    # This should deal the first two cards
    deck = Deck()

    deck.deal(player1)
    deck.deal(player2)

    player1.display_cards()
    player2.display_cards()

    while True:
        # This is the Players Hand
        if player1.value > 21:
            print("You busted")
            break

        choice = input("Would you like to hit or stay?  (Hit/Stay").lower()

        if choice == 'hit':
            deck.deal(player1)
            player1.calculate_value()
        elif choice == 'stay':
            player1.play = 'stay'
            break
        else:
            print("Please choose a valid option. ")
            continue

        player1.display_cards()

        # This is the Dealers Hand

        if player2.value <= 16:
            print("Dealer Hits")
            deck.deal(player2)
            player2.calculate_value()
            player2.play = 'hit'

        if player2.value > 21:
            print("Dealer Busted")
            break
        elif player2.value > 16:
            player2.play = 'stay'
        player2.display_cards()

        if player2.play == 'stay' and player1.play == 'stay':
            break
    game.compare(player1, player2)

    for card in player2.cards:
        print(card, '\n')

    play_again = input("would you like to play again> (y/n) ")

    if play_again == 'n':
        game.playing = False
        print("Thanks for playing")
    elif play_again == 'y':
        game.playing = True
