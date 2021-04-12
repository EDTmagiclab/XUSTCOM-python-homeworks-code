def dect(x,y):
    l=list(x)
    if y in l:
        return True
    else:
        return False
x=input('x')
y=input('y')
e=dect(x,y)
print(e)
