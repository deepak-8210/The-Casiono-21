import random
suits = ('spade','diamond','heart','club')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','ten','ten','ten')
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'Ace':1 or 11}

class Card:
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.value = values[ranks]
    
    def __str__(self):
        return self.suit + ' of ' + self.rank

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(rank,suits)
                created_card.append(self.all_cards)

    def deck_shuffle(self):
        return self.all_cards.shuffle

    def deal_one(self):
        return self.all_cards.pop(0)
    
    def card_list(self):
        card_com = ' '
        for card in self.all_cards:
            card_com.append(card)

        print(card_com)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        if self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1

class chips:
    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('how many chips do you want to bet? '))
        except ValueError:
            print("sorry, your bet can't exceed",chips.total)
        else:
            if chips.bet > chips.total:
                print('sorry,a bet must be an integer')
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):

    global playing

    while True:
        x = input("would you like to hit or stand?")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("player stands. Dealer is playing")
            playing = False
        else:
            print("sorry, please try agin.")
            continue
        break

def show_some(player,dealer):
    print('\n dealer hand')
    print('<card hidden>')
    print('',dealer.hand[1])
    print('\n Player hand:', *player.card, sep = '\n')
 
def show_all(player,dealer):
    print('\nDealer hand:', *dealer.hand, sep = '\n')
    print('dealer hand =',dealer.value)
    print('\nPlayers card:',*player.cards,sep = '\n')
    print('players hand =',player.value)

def player_busts(player,dealer,chips):
    print('player busts!')
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print('player wins!')
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print('Dealer busts!')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print('dealer wins!')
    chips.lose_bet()
def push(player,dealer):
    print("dealer and player tie! it's a push.")

    

while True:
    print("Welcome to BlackJack! Get as close to 21,Dealer hits untill he reaches 17.Aces count as 1 or 11")

    deck = Deck()
    deck.shuffle()

    Player_hand = Hand()
    Player_hand.add_card(deck.deal_one())
    Player_hand.add_card(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    player_chips = chips()

    take_bet(player_chips)
    
    show_some(Player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,Player_hand)
        show_some(Player_hand,dealer_hand)

        if Player_hand.value > 21:
            player_busts(Player_hand,dealer_hand,player_chips)
            break

    if Player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(Player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(Player_hand,dealer_hand,player_chips)
        
        elif dealer_hand.value > Player_hand.value:
            dealer_wins(Player_hand,dealer_hand,player_chips)
        
        elif dealer_hand.value < Player_hand.value:
            player_wins(Player_hand,dealer_hand,player_chips)

        else:
            push(Player_hand,dealer_hand)

    print("\n Player's winnings stand at",player_chips)

    new_game = input("would you like to play another game")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("thanks for playing!")
        break
              