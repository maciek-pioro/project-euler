# def preceeding(a, b):
#     if b==0:
#         return [a-1]
f = open('Euler 18.txt')
arr = []
for i in f:
    arr.append(i)
arr2=[]
for i in arr:
    arr2.append(i.rstrip('\n'))
arr3=[]
for i in arr2:
    arr3.append(i.split(' '))
arr3[0][0]=int(arr3[0][0])
for i in range(1, len(arr3)):
    for j in range(0, len(arr3[i])):
        print(i, j)
        if j==0:
            arr3[i][j]=int(arr3[i][j])+arr3[i-1][j]
        elif j==len(arr3[i])-1:
            arr3[i][j]=int(arr3[i][j])+arr3[i-1][j-1]
        else:
            arr3[i][j]=int(arr3[i][j])+max(arr3[i-1][j],arr3[i-1][j-1])
print(arr3)