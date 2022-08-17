import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card():
    '''
    Card creates an objects consisting of suits and ranks
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    '''
    An object of Deck consisting 52 cards of 4 different suits and 13 different ranks
    '''

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                # To be evaluated !
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    '''
    Object in which the
    '''

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    '''

    '''

    def __init__(self, total):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    '''
    A function which takes 1 argument - chips -
    and places a bet considering whether you have enough amount of chips
    assigned to your account
    '''
    while True:
        try:
            chips.bet = int(input("How much would you like to bet? "))
        except:
            print("Looks like you entered an invalid value - please try again.")
        else:
            if chips.bet > chips.total:
                print(
                    f"It looks like you don't have enough chips for a bet - {chips.total} please enter your bet again.")
                continue
            else:
                print(f"Your bet - {chips.bet} chips - has been accepted.")
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def double_down(deck,hand,chips):
    while True:
        try:


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        answer = input("Would you like to hit or stand? Enter 'h' or 's'")
        if answer[0].lower() == 'h':
            hit(deck, hand)
        elif answer[0].lower() == 's':
            print('Player stands. Dealer is playing')
            playing = False
        else:
            print("Invalid character. Please enter again.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<hidden card>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n")


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("\nPlayer's Hand:", *player.cards, sep="\n")


def player_busts(chips):
    chips.lose_bet()
    print("Player Busts")


def player_wins(chips):
    chips.win_bet()
    print("Player wins!")


def dealer_busts(chips):
    chips.win_bet()
    print("Dealer busts!")


def dealer_wins(chips):
    chips.lose_bet()
    print("Dealer wins!")


def push():
    print("Player and dealer tie. It's a push")


# Chips deposit
player_deposit = int(input("Please enter how many chips would you like to start with?: "))

# Set up the Player's chips
player_chips = Chips(player_deposit)

# Game logic
while True:
    print("Welcome to Blackjack game!")
    playing = True

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

    # First deal
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())

    # Second deal
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # Player_busts if his hands exceeds value of 21
        if player.value > 21:
            player_busts(player_chips)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer.value < 17:
            hit(deck, dealer)

        # Show all cards
        show_all(player, dealer)

        # Run different winning scenarios

        if dealer.value > 21:
            dealer_busts(player_chips)
        elif dealer.value > player.value:
            dealer_wins(player_chips)
        elif player.value > dealer.value:
            player_wins(player_chips)
        else:
            push()

        # Inform Player of their chips total
        print(f"\nYou still have {player_chips.total} chips.")

        # Ask to play again

        while True:
            answer = input("Would you like to play again? (y/n)")
            if answer[0].lower() == "y":
                playing = True
            elif answer[0].lower() == 'n':
                playing = False
            else:
                continue
            break
        break