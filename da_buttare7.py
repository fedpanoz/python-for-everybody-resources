fname = input("Enter file name: ")
fh = open(fname)
words = []
for line in fh:
    lista = line.split()
    for x in lista:
        if x not in words:
            words.append(x)

print(sorted(words))
