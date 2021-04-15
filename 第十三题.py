def fib(a,b,n):
    if n==1:
        return a
    if n==2:
        return b
    return fib(b,a+b,n-1)
max=0
i=1
n=0
while True:
    max=fib(1,1,i)
    if max>=5000:
        print(n)
        break
    n=max
    i=i+1