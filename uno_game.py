completeDeck=[]
colori = ["rosso", "verde", "blu", "giallo"]
def GenerateDeck():
    newDeck = []
    for colore in colori:
        for numero in range(0, 11):
            newDeck.append(str(numero) + " " + colore)
    return newDeck


myDeck = GenerateDeck()

def anotherDeck():
    secondDeck=[]
    for colore in colori:
        for numero in range(1,11):
            secondDeck.append(str(numero)+" "+ colore)
    return secondDeck
secondDeck=anotherDeck()

completeDeck=myDeck+secondDeck
print(completeDeck)