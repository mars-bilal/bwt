testo = "banana"
testo = testo + "$"    
n = len(testo)

rotazioni = []
for i in range(n):
    rotazione = testo[i:] + testo[:i]
    rotazioni.append(rotazione)
    print(rotazione)

rotazioni.sort()

bwt = ""
for r in rotazioni:
    bwt = bwt + r[-1]

print(bwt)

bwt = "annb$aa"
n = len(bwt)

tabella = [""] * n

for giro in range(n):
    for i in range(n):
        tabella[i] = bwt[i] + tabella[i]
    tabella.sort()

originale = ""
for riga in tabella:
    if riga[-1] == "$":
        originale = riga[:-1]   # tolgo il "$"

print(tabella)   
