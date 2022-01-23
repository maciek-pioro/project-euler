def isPalindrom(num):
    if str(num)==str(num)[::-1]:
        return True
    else:
        return False

max=0
for i in range(100, 1000):
    for j in range(100, i+1):
        if isPalindrom(i*j) and i*j>max:
            max=i*j
print(max)    