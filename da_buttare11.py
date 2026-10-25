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
        print(e[0])





  