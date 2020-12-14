#ax+by = gcd(a,b)
def extgcd(a,b,d = 0):#
    g = a
    if b==0:
        x,y = 1,0
    else:
        x,y,g = extgcd(b,a%b)
        x, y = y,  x - a // b * y
    return x,y,g