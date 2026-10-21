# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
somma = 0
conto_linea = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        colonpos = line.find(':')
        line = line[colonpos + 1:]
        conv = float(line)
        somma = somma + conv
        conto_linea += 1
        media = somma / conto_linea
print(media)
print("Done")
