array=[[0]]
for i in range(21):
    array.append([0])
for i in range(21):
    for j in range(21):
        array[i].append(0)
for i in range(21):
    for j in range(21):
        if i==0:
            array[i][j]=1
        if j==0:
            array[i][j]=1
        if i!=0 and j!=0:
            print(i)
            array[i][j]=array[i-1][j]+array[i][j-1]
print(array)