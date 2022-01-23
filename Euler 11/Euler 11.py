f=open('Euler 11.txt', 'r')
ans=0
arr=[]
for i in f:
    arr.append(i)
tmp=arr[:]
arr=[]
for i in tmp:
    arr.append(i.rstrip('\n'))
tmp=arr[:]
arr=[]
for i in tmp:
    arr.append(i.split(' '))
tmp=arr[:]
arr=[]
for i in range(20):
    arr.append([])
    for j in range(20):
        arr[i].append(int(tmp[i][j]))
ans=0
for i in range(17):
    for j in range(20):
        ans=max(ans, arr[i][j]*arr[i+1][j]*arr[i+2][j]*arr[i+3][j])
for i in range(20):
    for j in range(17):
        ans=max(ans, arr[i][j]*arr[i][j+1]*arr[i][j+2]*arr[i][j+3])
for i in range(17):
    for j in range(17):
        ans=max(ans, arr[i][j]*arr[i+1][j+1]*arr[i+2][j+2]*arr[i+3][j+3])
for i in range(3, 20):
    for j in range(17):
        ans=max(ans, arr[i][j]*arr[i-1][j+1]*arr[i-2][j+2]*arr[i-3][j+3])
print(ans)