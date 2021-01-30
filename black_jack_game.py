import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Card():

    def __init__(self, suit, rank):
        self.mysuit = suit
        self.myrank = rank

    def __str__(self):
        return f"{self.myrank} of {self.mysuit}."


class Deck():

    def __init__(self):
        self.mydeck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                made_card = Card(suit, rank)
                self.mydeck.append(made_card)

    def __str__(self):
        print("A new deck has been created.")
        deck_list = ''
        for card in self.mydeck:
            deck_list += '\n' + card.__str__()
        return f"The deck has {deck_list}"

    def shuffle_deck(self):
        print("The deck has been shuffled thoroughly.")
        random.shuffle(self.mydeck)

    def deal(self):
        self.mydeck.append(self.mydeck.pop(0))
        return self.mydeck.pop(0)

class Hand():
    def __init__(self):
        self.mycards = []  # start with an empty list as we did in the Deck class
        self.myvalue = 0   # start with zero value
        self.myaces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        print("Adding a new card to the hand.")
        self.mycards.append(card)
        self.myvalue += values[card.myrank]

        if card.myrank == "Ace":
            self.myaces += 1


    def adjust_for_ace(self):
        #IF TOTAL VALUE > 21 AND ACE IS THERE, THEN CHANGE ACE TO HAVE VALUE OF 1.
        while (self.myvalue > 21) and (self.myaces > 0):
            self.myvalue -= 10
            self.myaces -= 1
    
'''
game_deck = Deck()
game_deck.shuffle_deck()

test_player = Hand()
pulled_card = game_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.myvalue)
pulled_card = game_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.myvalue)
print(test_player.myaces)
'''

class Chips():

    def __init__(self, starting=1000):
        self.mytotal = starting  # This can be set to a default value or supplied by a user input
        self.mybet = 0
    
    def __str__(self):
        return f"There are {self.mytotal} dollars worth of available chips."

    def win_bet(self):
        self.mytotal += self.mybet

    def lose_bet(self):
        self.mytotal -= self.mybet


def take_bet(chips):
    
    while True:
        bet = int(input("How much do you wish to raise in a bet?"))
        if (chips.mytotal > bet):
            chips.mybet += bet
            break
        elif (chips.mytotal < bet):
            print("Your bet cannot exceed your bankroll amount. Try again.")
            continue
    
def hit(deck, hand):
    print("Hit has been chosen.")
    card_draw = deck.deal()
    hand.add_card(card_draw)
    hand.adjust_for_ace()
    

def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        ask = input("Do you want to hit or stand?")
        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print('Player has chosen to pass this turn.')
            playing = False
        
        else:
            print("Sorry, unable to understand input, please try again.")
        
        break

def show_some(player, dealer):
    print("\n Dealer's hand: ")
    print("<card hidden>")
    print(dealer.mycards[1])
    print("\n Player's hand: ", *player.mycards, sep = "\n")


def show_all(player, dealer):
    print("\n Dealer's hand: ", *dealer.mycards, sep="\n")
    print("Dealer's hand's value = ", dealer.myvalue)

    print("\n Player's hand: ", *player.mycards, sep="\n")
    print("Player's hand's value = ", player.myvalue)


def player_busts(player, dealer, chips):
    print("Player busted!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busted!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Player and Dealer tied. Push!")


##GAMEPLAY LOGIC CONSTRUCTION

##OPENING STATEMENT
print("Welcome to a game of Blackjack. Please have a seat. Get as close to 21 as you can without going over! Dealer hits until she reaches 17. Aces count as 1 or 11.")

#CREATE THE DECK AND SHUFFLE IT.
game_deck = Deck()
game_deck.shuffle_deck()

##SET UP 2 HANDS, ONE FOR PLAYER AND ONE FOR DEALER.
player_hand = Hand()
player_hand.add_card(game_deck.deal()) ##ADDING 2 CARDS TO PLAYER'S HAND.
player_hand.add_card(game_deck.deal())

dealer_hand = Hand()
dealer_hand.add_card(game_deck.deal())##ADDING 2 CARDS TO DEALER'S HAND.
dealer_hand.add_card(game_deck.deal())

##CREATE THE PLAYER'S SET OF CHIPS.
player_chips = Chips(5000)
print(player_chips)

##TAKE THE PLAYER'S BET.
take_bet(player_chips)

##SHOW CARDS BUT KEEP ONE OF DEALER'S CARDS HIDDEN.
show_some(player_hand, dealer_hand)

while playing:

    ##ASK PLAYER FOR HIT OR STAND.
    hit_or_stand(game_deck, player_hand)
    ##SHOW CARDS PARTIALLY AGAIN.
    show_some(player_hand, dealer_hand)
    #IF PLAYER'S POINTS EXCEED 21, PLAYER BUSTS AND LOOP BREAKS.
    if player_hand.myvalue > 21:
        player_busts(player_hand, dealer_hand, player_chips)
        break

    ##IF PLAYER HAS NOT BUSTED, PLAY DEALER'S HAND UNTIL DEALER GETS 17.
    if player_hand.myvalue <= 21:
        while dealer_hand.myvalue < player_hand.myvalue:
            hit(game_deck, dealer_hand)

            ##SHOW ALL THE CARDS.
            show_all(player_hand, dealer_hand)

            ##RUN ALL THE GAME SCENARIOS.
            if dealer_hand.myvalue > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.myvalue > player_hand.myvalue:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.myvalue < player_hand.myvalue:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)
    
    ##INFORM PLAYER OF THE TOTAL CHIPS.
    print(f"\n The player's winning stands at ${player_chips.mytotal}.")

    new_game = input("Would you like to play another hand?")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing.")
        break






