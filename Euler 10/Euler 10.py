import math
def isPrime(p):
    if p==1:
        return False
    if p==2:
        return True
    for i in range(2, math.ceil(math.sqrt(p))+1):
        if p%i==0: return False
    return True

sum=0
for i in range(1, 2000000):
    if isPrime(i):
        sum+=i
print(sum)