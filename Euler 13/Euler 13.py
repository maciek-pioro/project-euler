f=open('Euler 13.txt','r')
sum=0
for i in f:
    sum+=int(i)
print(sum)
s=''
for i in range(10):
    s+=str(sum)[i]
print(s)