dict1={}
b=0
n=0
for i in range (0,3):
    a=str(input("名字"))
    b=float(input("分数"))
    dict1[a]=b
a=dict1.values()
a=list(a)
a.sort()
for m in a:
    n=n+m
    c=n/3
print( "最高分%s分" % a[2])
print("最底分%s分" % a[0])
print("平均分%s分" % c)
