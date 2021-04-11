
for i in range(1,1001):
    q=0
    for n in range(1,i):
        if i%n==0 and i!=n:
            q=q+n
    if q==i:
        print(q)


