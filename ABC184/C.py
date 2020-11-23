r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
if r1==r2 and c1==c2:print(0);exit()
if r1-c1==r2-c2 or r1+c1==r2+c2:
    print(1)
    exit()
if abs(r1-r2)+abs(c1-c2)<=3:
    print(1);exit()
if (c1+c2+r1-r2)%2==0 and (r1+r2+c1-c2)%2==0:
    print(2);exit()
if (c1+c2+r2-r1)%2==0 and (r1+r2+c2-c1)%2==0:
    print(2);exit()
else:
    for x in range(-3,4):
        for y in range(-3,4):
            X = r2+x
            Y = y+c2
            if abs(X-r2)+abs(Y-c2)<=3 and X+Y==r1+c1 or X-Y==r1-c1:
                print(2);exit()
    print(3);exit()
