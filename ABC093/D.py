from math import floor
q = int(input())
ab=[list(map(int,input().split())) for _ in range(q)]
for a,b in ab:
    if a==b:
        print(2*a-2)
        continue
    t = floor((a*b)**0.5)
    if t*t >=a*b:
        print(2*t-3)
    elif t*(t+1)>=a*b:
        print(2*t-2)
    else:
        print(2*t-1)
    