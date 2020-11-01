n,m = map(int,input().split())
cnt = [0]*(10**5+1)
L = []
ans = ['']*(10**5+1)
for i in range(m):
    p,y = map(int,input().split())
    L.append([y,p,i+1])
L.sort()
for y,p,i in L:
    P = str(p).zfill(6)
    cnt[p]+=1
    x = cnt[p]
    X = str(x).zfill(6)
    ans[i] = P+X
for a in ans:
    if a:
        print(a)