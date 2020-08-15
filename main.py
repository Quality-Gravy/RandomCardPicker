import tkinter as tk
from tkinter import *
from card import *
from mainFunctions import * #import all of the main functions

root = tk.Tk() #the main root tk window

#set the basic window functions
root.title("Random Card Picker")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="#00700d")

#create a frame
frame = tk.Frame(root)
frame.pack()





image_frame = tk.Frame(root)
#create an canvas to hold an image frame
image_canvas = tk.Canvas(image_frame, width=500, height=500)



def updateCardLabel():
    #create the card label
    card_label = tk.Label(root, justify=LEFT, text=getCapitalCardName(current_card[0].name),
    font='Georgia', bg="#d9d9d9", borderwidth=3, width=20, relief='sunken', padx=10, pady=10)
    #card_label.place()
    card_label.place(relx=.5, rely=.8, anchor=CENTER)

def createCardImage():
    card = tk.PhotoImage(file=getRandomCard())
    card = card.zoom(9)
    card = card.subsample(32)
    label = Label(image=card, relief='sunken')
    label.place(relx=.305,rely=.10)
    image_canvas.create_image(20, 20, image=card)
    image_canvas.image = card
    image_canvas.pack()
    updateCardLabel()
    print("Initted image")


def getRandomCardFinal():
    getRandomCard()
    createCardImage()
    updateCardLabel()

#set the button to get a random card
main_but = tk.Button(frame, text="Get Random Card", font="Georgia", relief='raised', command=getRandomCardFinal)
main_but.pack()



#createCardImage() #create a card image


root.mainloop() #the mainloop of the application
