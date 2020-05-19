import random
colors = ["rosso", "verde", "blu", "giallo"]
def generateDeck():
    # mazzo da 0 a 10
    newDeck = []
    for color in colors:
        for numero in range(0, 10):
            newDeck.append(str(numero) + " " + color)
    # secondo mazzo da 1 a 10
    for color in colors:
        for numero in range(1,10):
            newDeck.append(str(numero)+" "+ color)
    #carte speciali
    i = 0
    while i < 4:
        newDeck.append("cambia colore")
        newDeck.append("+ 4")
        i += 1
    c=0
    for color in colors:
        while c<2:
            newDeck.append(color + " stop")
            newDeck.append(color + " invert")
            newDeck.append(color + " +2")
            c+=1
    random.shuffle(newDeck)
    return newDeck

myDeck = generateDeck()

#def popCard(deck):
#   card = deck[0]
#    deck.remove(deck[0])
#    return card

def drawCard(showOutput):
    card = myDeck.pop(0)
    myHand.append(card)
    if showOutput: # == True
        print("Hai pescato " + card)

myHand = []
hisHand = []
def initHands(): #initialize
    i=0
    while i<7:
        drawCard(False) # ti fa pescare la carta
        hisHand.append(myDeck.pop(0))
        i+=1
initHands()
print(myHand)
print(hisHand)

#solo alberto può modificare

