n,m = map(int,input().split())
L = []
for _ in range(m):
    l,r = map(int,input().split())
    L.append([l,r])
L.sort()
s,t = L[0]
for i in range(1,m):
    l,r = L[i]
    if t<l:print(0);exit()
    if r>=t:
        s = l
    else:
        s = l
        t = r

print(t-s+1)
