suit=('HEARTS','SPADES','DIAMONDS','CLUBS')
rank=('ace','two','three','four','five','six','seven','eight','nine','ten','king','queen','jack')
value={'ace':11,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'king':10,'queen':10,'jack':10}

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for sui in suit:
            for ran in rank:
                created = Card(sui, ran)
                self.all_cards.append(created)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def pop_one(self):
        single = self.all_cards.pop(0)
        return single

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += value[card.rank]

def hit(deck, hand):
    single = deck.pop_one()
    hand.add_card(single)

def hit_stand(deck, hand):
    global play
    while True:
        x = int(input("Hit or stand? 1 for Hit, 2 for Stand: "))
        if x == 1:
            hit(deck, hand)
        elif x == 2:
            play = False
            break
        else:
            print("Sorry, I can't understand. Please enter 1 or 2.")
            continue

def show_some(player, computer):
    print("\nComputer's hand:")
    print("First card is hidden")
    print(computer.cards[1])
    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)

def show_all(player, computer):
    print("\nComputer's hand:")
    for card in computer.cards:
        print(card)
    print(f"Computer's score is {computer.value}")
    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)
    print(f"Player's score is {player.value}")

play = True

while play:
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>WELCOME TO AKSHAY'S CARD <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n")
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.pop_one())
    player_hand.add_card(deck.pop_one())
    computer_hand = Hand()
    computer_hand.add_card(deck.pop_one())
    computer_hand.add_card(deck.pop_one())
    show_some(player_hand, computer_hand)
    while play:
        hit_stand(deck, player_hand)
        show_some(player_hand, computer_hand)
        if player_hand.value > 21:
            print("\nCOMPUTER WINS!")
            break
    if player_hand.value <= 21:
        while computer_hand.value <= 19:
            hit(deck, computer_hand)
        show_all(player_hand, computer_hand)
        if computer_hand.value > 21:
            print("\nPLAYER WINS!")
        else:
            if computer_hand.value > player_hand.value:
                print("\nCOMPUTER WINS!")
            elif computer_hand.value < player_hand.value:
                print("\nPLAYER WINS!")
            else:
                print("\nTIE MATCH!")
    new_one = int(input("Want to play another round? 1 for Yes, 2 for No: "))
    if new_one == 1:
        play = True
    else:
        print("Thanks for playing!")
        play = False
