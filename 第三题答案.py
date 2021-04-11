a = 1
b = 1
pie = 0
q = 1
n = int(input("n"))
for i in range(0,n):
    q = a / b
    pie=pie+q
    b = ((-1)**(i-1))*(2+abs(b))
r = 4*pie
print(r)