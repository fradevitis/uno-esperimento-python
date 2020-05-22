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
            newDeck.append("special " + color + " stop")
            newDeck.append("special " + color + " invert")
            newDeck.append("special " + color + " +2")
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

lastThrow = myDeck.pop(0)
print("Ultima carta buttata: " + lastThrow)

def CheckAction(card): # card = 5 rosso
    splittedCard = card.split(" ")
    print(splittedCard)
    splittedLastThrow = lastThrow.split(" ")
    print(splittedLastThrow)
    if splittedCard[0] == splittedLastThrow[0] or splittedCard[1] == splittedLastThrow[1]:
        print("puoi buttare " + card)
        return True
    else:
        return False
    

def PlayerAction():
    print("In mano hai: ")
    for x in range(0, len(myHand)):
        print(str(x) + " " +  myHand[x])
    action = int(input("inserisci il numero della carta che vuoi buttare "))
    if CheckAction(myHand[action]) == True:
        print("Carta giocata")
    else:
        print("La carta non puo essere giocata")

PlayerAction()

