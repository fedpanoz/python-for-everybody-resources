name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
nomi = {}
handle = open(name)
counter = 0
max_key = ''
for line in handle:
    if line.startswith('From '):
        riga = line.split()
        indirizzo = riga[1]
        nomi[indirizzo] = nomi.get(indirizzo, 0) + 1
for a, b in nomi.items():
    if  b > counter:
        counter = b

print(counter)
