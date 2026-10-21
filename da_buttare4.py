txt = 'but soft what light through yonder window breaks'
words = txt.split()
#print(type(words))

t = list()
for word in words:
    t.append((len(word),word))
t.sort(reverse=True)
print(type(t))
print(t)

res = list()
for lenght, word in t:
    res.append(word)

print(res)