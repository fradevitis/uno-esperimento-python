import random
colori=["giallo", "rosso", "blu", "verde"]
def build():
    mazzocompleto=[]
    for x in range(0,10):
        for colore in colori:
            mazzocompleto.append(str(x)+" "+ colore)
    for y in range(1,10):
        for colore in colori:
            mazzocompleto.append(str(y)+" "+ colore)
    for colore in colori:
        i=0
        while i<2:
            mazzocompleto.append("stop "+ colore)
            mazzocompleto.append( "cambio giro "+ colore)
            mazzocompleto.append("+2 " + colore)
        i+=1
    random.shuffle(mazzocompleto)
    return mazzocompleto
build()
DECK=mazzocompleto
print(DECK)
