import math 
for i in range(10000): 
#转化为整型值 
    x = math.sqrt(i + 100)
    y = math.sqrt(i + 268)
    
    if(x==int(x)) and (y == int(y)):
        print(i)
        break

