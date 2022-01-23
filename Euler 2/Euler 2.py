sum=0
i=1
j=1
while j<=4000000:
    p=j
    j+=i
    i=p
    if j%2==0:
        sum+=j
print(sum)    