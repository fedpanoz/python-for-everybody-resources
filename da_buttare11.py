name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dizio = {}
freq = 0
for line in handle:
    if line.startswith('From '):
        c = line.split()
        d = c[5]
        e = d.split(':')
        #print(e[0])
        f = e[0]
        dizio[f] = dizio.get(f, 0) + 1
#print(dizio)
for ho, val in sorted(dizio.items()):
    print(ho, val)

  