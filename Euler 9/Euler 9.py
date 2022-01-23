for c in range(1, 1000):
    for b in range(1, c):
        for a in range(1, b+1):
            if c**2 == a**2+b**2 and a+b+c == 1000:
                print(a * b * c)
                exit()
