import math
l=600851475143
while l>1:
    i=2
    while l%i!=0:
        i+=1
    l=l/i
print(i)