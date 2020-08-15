import random
from card import *
from deck import *

current_deck = Deck() #create a new deck

#pick a random card from the specified deck
def pickRandomCard(dck):
    return random.choice(dck.cards)
