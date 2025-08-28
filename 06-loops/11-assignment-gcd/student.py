def gcd(x, y):
    x = abs(x)
    y = abs(y)

    for i in range(min(x,y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i