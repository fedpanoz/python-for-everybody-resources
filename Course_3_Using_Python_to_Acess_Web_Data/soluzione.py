import re
testo = open("sample_data.txt")
lista_numeri = []
for line in testo:
    x = re.findall("[0-9]+", line)
    if len(x) > 0:
        lista_numeri.append(x)

totale = 0
for sottolista in lista_numeri:
    for string_num in sottolista:
        numero = int(string_num)
        totale += numero
    

print(totale)


