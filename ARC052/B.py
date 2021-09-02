import math

def f(r,h):
    return (r**2) * math.pi * h / 3

N,Q = map(int,input().split())

XRH = []

for i in range(N):

    X,R,H = map(int,input().split())
    XRH.append((X,R,H))

for i in range(Q):

    A,B = map(int,input().split())
    ans = 0

    for x,r,h in XRH:

        if x+h <= A or B <= x:
            continue
        elif A <= x <= x+h <= B:
            ans += f(r,h)
        elif x <= A <= x+h <= B:
            newh = x+h-A
            newr = r * newh / h
            ans += f(newr,newh)
        elif A <= x <= B <= x+h:
            newh = x+h-B
            newr = r * newh / h
            ans += f(r,h) - f(newr,newh)
        else: # x <= A <= B <= x+h
            h2 = x+h - B
            r2 = r * h2 / h
            h3 = x+h - A
            r3 = r * h3 / h
            ans += f(r3,h3) - f(r2,h2)

    print (ans)
    
