def collatz(n):
    if n==1:
        return 0
    if n%2==0:
        return int(n/2)
    else:
        return 3*n+1

cmax=0
ans=1
array = [0]
for i in range(1, 1000001):
    count=0
    m=i
    while m>1:
        m=collatz(m)
        count+=1
        if m<i:
            count+=array[m]
            m=1
    array.append(count)
    if count>cmax:
        ans=i
        cmax=count
print(ans)