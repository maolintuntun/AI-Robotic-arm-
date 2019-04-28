from math import sqrt
from sys import stdout


a=0
#a为素数个数
#每次找到一个素数，b就加一 用来求素数的总个数
for m in range(101,201):
    b=1
    for i in range(2, int(sqrt(m)) + 1):
        if m % i == 0:
            b = 0
            break
    if b==1:
        print ('%-4d' % m)
    a=a+b
    if a%10==0:
        print('')
    
print('The total is %d' % a)



    
