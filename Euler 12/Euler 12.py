import math

def isSquare(n):
    if math.sqrt(n)==int(math.sqrt(n)):
        return True
    else:
        return False
def divisorsNum(n):
    count=0
    i=1
    while i<=math.sqrt(n):
        if n%i==0:
            count+=2
        i+=1
    if isSquare(n):
        return count-1
    else:
        return count
def trigNum(n):
    return int(n*(n+1)/2)

n=1
div=0
while div<=500:
    n+=1
    if n%2==0:
        div=divisorsNum(n/2)*divisorsNum(n+1)
    else:
        div=divisorsNum(n)*divisorsNum((n+1)/2)
print(trigNum(n))