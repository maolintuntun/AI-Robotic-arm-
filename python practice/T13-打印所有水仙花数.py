import math
for n in range(100,999):
    a=int(n/100)
    b=(int(n/10))%10
    c=n%10
    if n==a**3+b**3+c**3:
        print (n)
