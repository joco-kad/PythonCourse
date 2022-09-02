meineliste = []
for i in range(1, 1001):
    meineliste.append(str(i))

for i in range(0, len(meineliste), 42):
    print(meineliste[i])    

def dummy_generator(n):
    i=0
    while i < n:
        if i%42 == 0:
            yield i +1
        i += 1

for i in dummy_generator(1000):
    print(i)

def clever_generator(n):
    i=1
    while i < n:
        yield i
        i += 42

for i in clever_generator(1000):
    print(i)

