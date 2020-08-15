import picker #import the picker python file'
from card import *
from deck import *

current_deck = Deck() #the deck that the application is using

card = Card("spades", "ace")

current_card = [card]

#turn a card name into a capital (ex. ace of spades - Ace of Spades)
def getCapitalCardName(card_name):
    word_list = card_name.split()
    final_word = ""
    for x in range(len(word_list)):
        if(x != 1):
            word = word_list[x]
            first_letter = word[0]
            new_word = (first_letter.upper() + word[1:])
            final_word += new_word
        else:
            final_word += " of "
    return final_word



#responsible for getting a random card and setting all of the labels correctly
def getRandomCard():
    new_card = current_deck.getRandomCard()
    print("You got " + str(new_card.name))
    current_card.clear()
    current_card.append(new_card)
    return new_card.getCardImageFilepath()

#print(getCapitalCardName("ace of spades"))
