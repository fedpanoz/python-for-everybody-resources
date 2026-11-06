name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
nomi = {}
handle = open(name)
counter = 0
max_key = ''
lista_valori = []
for line in handle:
    if line.startswith('From '):
        riga = line.split()
        indirizzo = riga[1]
        nomi[indirizzo] = nomi.get(indirizzo, 0) + 1
for b in nomi.values():
    lista_valori.append(b)
for x in lista_valori:
    if x > counter:
        counter = x
lillo = lista_valori.index(counter)   
for a, b in nomi.items():
    if b == counter:
        print(a, b)
