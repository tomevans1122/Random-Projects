import random
from IPython.display import clear_output


# Create global tuples and dictionary for card suits, ranks and corresponding values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
###############################################################################


#DEFINING CLASSES FOR CARD, DECK, PLAYER AND POT

# Class for specific cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit            # rank of card
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
        
###################################################################################################
# Class for the whole deck and its operations        
class Deck:
    
    def __init__(self):
        self.deck = []            #Empty list (so far) of cards
        for suit in suits:   # for particular suit
            for rank in ranks:                         # for value of card in each suit
                self.deck.append(Card(suit,rank))       # appends list of cards with cards built from this function
                
    def show_card(self):
        for card in self.deck:           # function to show all cards now in self.cards after build(self)
            card.show_card()
            
    def shuffle(self):            # function to shuffle cards in deck
        
        random.shuffle(self.deck) #imports random library which has a shuffling algorithm

      
            
    def deal(self):                    # function to draw card from deck
        return self.deck.pop()             # pops random card out of deck
    
########################################################################################################

#Class for player's hand
class Hand:
    def __init__(self):
        self.cards = []             # Empty list for cards in hand
        self.value = 0
        self.aces = 0          # attribute to keep track of aces
        
    def add_card(self, card):
        # Function to draw card from deck
        # card passed in will be from Deck.deal()
        self.cards.append(card)  # Appends self.cards list to account for card drawn
        self.value += values[card.rank]
        
        #track aces when card is pulled from deck
        if card == 'Ace':
            self.aces += 1
            
            
    def adjust_for_aces(self):
        #if total value > 21 and I still have an ace --> change ace value to 1 instead of 11
        while self.value > 21 and self.aces: # uses truthiness, all number but zero counts as true
            self.value -= 10
            self.aces -= 1
            

###########################################################################################################

# Money pot class
class Chips():
   
    def __init__(self, total=100):
        self.total = total     # gives balance in pot
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet

#################################################################################################################
# FUNCTIONS

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)



# Takes first bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet this game? "))
        except:
            print("Sorry, please provide an integer.")
        else:
            if chips.bet > chips.total:
                print(f"You do not have enough chips! You have {chips.total} chips!")
            else:
                break
                
                
    
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()
    
    
    
def hit_or_stand(deck, hand):
    global playing #to control upcoming while loop
    
    while True:
        x = input("Hit or stand? Enter 'h' or 's' ")
        if x.lower()[0] == 'h':
            hit(deck,hand)
        elif x.lower()[0] == 's':
            print("Player stands. Dealer's turn.")
            playing = False
        else:
            print("I didn't understand that, please enter 'h' or 's' only!")
            continue
        break
        

def push(player, dealer):
    print("Player and dealer are tied! PUSH!")
    
def player_bust(player, dealer, chips):
    print("Player loses!")
    chips.lose_bet()
    
def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()
    
def dealer_bust(player, dealer, chips):
    print("Dealer busts! Player wins!")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


#############################################################

############ G A M E P L A Y ################################


while True:
    print("Welcome to Blackjack!") #welcome message
    
    # Create an instance of the deck and shuffle it
    deck = Deck()
    deck.shuffle()
    
    # Create a player hand and add to it twice
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    # Create a dealer hand and add to it twice
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Create an instance of chips for the player
    player_chips = Chips()
    
    #Take the player's first bet
    take_bet(player_chips)
    
    #Show the player's cards and only one of the dealer's cards
    show_some(player_hand,dealer_hand)
    
    # start of game
    while playing:
        # Ask player if he wants to hit or stand
        hit_or_stand(deck, player_hand)
        
        # Show the cards of the player, still only showing one of the dealer
        show_some(player_hand, dealer_hand)
        
        # if player cards are worth more than 21, they lose
        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            
            break
            
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
            
        show_all(player_hand, dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand, player_chips)
            
        elif dealer_hand.value < 21 and player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            
        elif dealer_hand.value <= 21 and dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
            
    print(f"Player chips are at {player_chips.total}")
    
    new_game = input("Would you like to play another hand? ")
    if new_game.lower()[0] == 'y':
        playing = True
        continue
    else:
        print("Thankyou for playing!")
        
        break