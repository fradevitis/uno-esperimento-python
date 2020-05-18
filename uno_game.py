def GenerateDeck():
    colori = ["rosso", "verde", "blu", "giallo"]
    newDeck = []
    for colore in colori:
        for numero in range(0, 11):
            newDeck.append(str(numero) + " " + colore)
    return newDeck


myDeck = GenerateDeck()
print(myDeck)
