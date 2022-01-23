first=100
sum=0
for i in range(1, first+1):
    for j in range(1, i):
        sum+=i*j
print(sum*2)