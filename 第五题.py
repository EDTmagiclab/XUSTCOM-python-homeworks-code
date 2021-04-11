import math
for i in range(100,1000):
   
    x=i//100 #百位
    y=i%10  #个位
    z=i//10%10 #十位
    if math.pow(x,2)+math.pow(y,2)+math.pow(z,2)==i//9:
        print(i)