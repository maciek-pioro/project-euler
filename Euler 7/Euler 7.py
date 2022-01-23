import math
def isPrime(p):
    if p==1:
        return False
    for i in range(2, math.ceil(math.sqrt(p))+1):
        if p%i==0: return False
    return True

n=10001
i=1
while n>1:
    i+=1
    if isPrime(i):
        n-=1
print(i)