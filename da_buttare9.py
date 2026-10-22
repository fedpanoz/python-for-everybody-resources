name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
nomi = {}
handle = open(name)
for line in handle:
    if line.startswith('From '):
        riga = line.split()
        indirizzo = riga[1]
        nomi[indirizzo] = nomi.get(indirizzo, 0) + 1
print(nomi)
