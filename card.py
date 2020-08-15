from card_images import card_images_front
#the card class, responsible for holding all of the information in a card
#card has 4 attributes:
#suite - CLUBS, SPADES, HEARTS, DIAMONDS
#number - 2 - ACE
#rank - NUMBER WHICH RANKS THE CARD FROM 1 - 21
#IMAGE - relies on image folder being in same directory

class Card:
    def __init__(self, suite, number, cardRank=None, name=None):
        self.suite = suite
        self.number = number
        self.cardRank = self.setCardRank()
        self.name = self.setName()

    #set the rank based on the suite and the number
    def setCardRank(self):
        number_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        special_ranks = ['jack', 'queen', 'king', 'ace']
        for x in number_ranks: #check to see if card number is a non-special rank
            if(str(self.number) == x):
                return x
        for x in special_ranks: #check for a special rank
            if(str(self.number) == x):
                if(x == 'jack'):
                    return str(11)
                elif(x == 'queen'):
                    return str(12)
                elif(x == 'king'):
                    return str(13)
                elif(x == 'ace'):
                    return str(14)

    #set the name of the card
    def setName(self):
        name = (str(self.number) + " of " + str(self.suite))
        return name

    #print the info of a card
    def printInfo(self):
        print(self.name)
        print(self.cardRank)

    #match an image with a card
    def getCardImageFilepath(self):
        #filename for ace of diamonds would be AD.png
        if(str(self.number) == str(10)):
            first_letter = str(10)
            second_letter = str(self.suite[0]).upper()
        else:
            first_letter = str(self.number[0]).upper()
            second_letter = str(self.suite[0]).upper()
        filename = str(first_letter + second_letter + ".png")
        filepath = str('card_images/card_images_front/' + filename)
        return filepath





#ace_of_clubs = Card("diamonds", "10")
#print(ace_of_clubs.getCardImageFilepath())
