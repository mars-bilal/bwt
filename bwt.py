stringa = "BANANA"
stringa = stringa + "$"

rotazioni = []

for i in range(len(stringa)):
    rotazione = stringa[i:] + stringa[:i]
    rotazioni.append(rotazione)
    print(rotazioni)

rotazioni.sort()

risultato = ""

for riga in rotazioni:
    risultato = risultato + riga[-1]

print(risultato)