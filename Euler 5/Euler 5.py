def gcd(a, b):
    if a<b:
        return gcd(b,a)
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a*b/gcd(a, b)

min=2
for i in range(2, 21):
    min=lcm(min, i)
print(min)