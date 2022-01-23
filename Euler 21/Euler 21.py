import math
# def ProperDivisors(n):
#     ans=[1]
#     for i in range(2, math.floor(math.sqrt(n)+1)):
#         if n%i==0:
#             ans.append(int(i))
#             ans.append(int(n/i))
#     if math.ceil(math.sqrt(n))==math.sqrt(n):
#         ans.remove(int(math.sqrt(n)))
#     return ans
# print(ProperDivisors(4))
def sumOfProperDivisors(n):
    ans=1
    for i in range(2, math.floor(math.sqrt(n)+1)):
        if(n%i==0):
            ans+=(i+n/i)
    if math.ceil(math.sqrt(n))==math.sqrt(n):
        ans-=math.sqrt(n)
    return int(ans)
sum=0
for i in range(2, 10001):
    if i==sumOfProperDivisors(sumOfProperDivisors(i)) and i!=sumOfProperDivisors(i):
        sum+=i
print(sum)