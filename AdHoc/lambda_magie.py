l=["aaa", "bbb", "ccc", "ddd"]
print(["Text_" + l[i] if i%2==0 else l[i] for i in range(len(l))])

f=lambda x: x**2
for i in range(10):
    print(f(i))

f=lambda i,ls,prefix: prefix + ls[i] if i%2==0 else ls[i]
print([f(i,l,"Text_") for i in range(len(l))])
