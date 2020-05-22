# formazione mazzo
import random
colori = ["rosso", "giallo", "verde", "blu"]
def costruisci():
    deck = []
    for number in range(0, 10):
        for colore in colori:
            deck.append(str(number) + " " + colore)
    for number in range(1, 10):
        for colore in colori:
            deck.append(str(number) + " " + colore)
    i = 0
    while i < 4:
        deck.append("cambio colore")
        deck.append("+4 carte")
    i += 1
    I = 0
    for colore in colori:
        while I < 2:
            deck.append("cambio giro " + colore)
            deck.append("stop giro " + colore)
            deck.append("+2 carte " + colore)
    I += 1
    random.shuffle(deck)
    return(deck)
Mazzo = costruisci()
#mani
def pescata(V):
    carta=Mazzo.pop(Mazzo[0])
    myhand.append(carta)
    if V:
        print("hai pescato "+ carta)
myhand=[]
hishand=[]
def mani():
    a=0
    while a<7:
        V=False
        pescata(V)
        hishand.append(Mazzo.pop(0))
    a+=1
mani()
terra=Mazzo.pop(0)
print(myhand)
def NC():
    terra.split()
    for carta in myhand:
        for x in range(0, len(myhand)):
            cartasplittata=carta.split()
        print(x + " "+ cartasplittata)
    if terra[0]==carta[0] or terra[1]==x[1]:
        print("puoi buttare "+x)
        True
    else:
        print("non puoi buttare "+x)
        False
NC()