import random
l=[]
for i in range(1,21):
    x=random.randint(1,100)
    l.append(x)
x=l[0:10]
y=l[10:20]
x.sort()
y.sort(reverse=True)
l=x+y
tuple(l)
print(l)