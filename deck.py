from card import Card #import the card class
import random

#deck includes a standard deck of cards with the jokers removed
class Deck:
    def __init__(self, cards=[]):
        self.cards = cards #the list of cards in the deck
        self.initCards() #add the cards to the deck

    def initCards(self):
        suites = ['clubs', 'spades', 'hearts', 'diamonds']
        list_of_numbers = ['2','3','4','5','6','7','8','9','10',
        'jack','queen','king','ace'] #list of all cards that need to be initialized
        for x in range(len(suites)):
            for c in range(len(list_of_numbers)):
                self.addCard(Card(suites[x], list_of_numbers[c]))

    def addCard(self,card):
        self.cards.append(card)

    #get a random card from the deck
    def getRandomCard(self):
        return random.choice(self.cards)

    #print basic info about the deck
    def printInfo(self):
        print(str(len(self.cards)) + " cards in deck")


st_deck = Deck() #create a deck
#st_deck.printInfo()
