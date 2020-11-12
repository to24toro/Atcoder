n = int(input())
A = []
for _ in range(n):
    x,y,h = map(int,input().split())
    A.append((x,y,h))
    if h > 0:
        a,b,c = x,y,h

for i in range(101):
    for j in range(101):
        H = c+abs(a-i)+abs(b-j)
        f = True
        for x,y,h in A:
            if h!=max(0,H-abs(x-i)-abs(y-j)):
                f = False
                break
        if f:
            print(i,j,H);exit()