import string
def takeApart(name):
    sum=0
    for letter in name:
        sum+=(string.ascii_lowercase.index(letter.lower())+1)
    return sum
f=open("p022_names.txt")
nameslist=[]
tmp=[]
tmp=f.read()
tmp=tmp.split(',')
ans=0
for name in tmp:
    nameslist.append((name.rstrip("\"")).lstrip("\""))
nameslist.sort()
l=len(nameslist)
for i in range(l):
    ans=ans+(takeApart(nameslist[i])*(i+1))
print(ans)
