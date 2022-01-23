import math
def sumOfProperDivisors(n):
    ans=1
    for i in range(2, math.floor(math.sqrt(n)+1)):
        if(n%i==0):
            ans+=(i+n/i)
    if math.ceil(math.sqrt(n))==math.sqrt(n):
        ans-=math.sqrt(n)
    return int(ans)
arr=[]
for i in range(5, 28124):
    if sumOfProperDivisors(i)>i:
        arr.append(i)
sum=0
sums=[False]*28140
for i in range(len(arr)):
    for j in range(i+1):
        if(arr[i]+arr[j]<28140):
            sums[arr[i]+arr[j]]=True
for i in range(28124):
    if sums[i]==False:
        sum+=i
print(sum)