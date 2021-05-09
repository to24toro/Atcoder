n,d,h = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(n)]
T.append([d,h])
T.sort()
L = []
for d,h in T:
    if not L:
        L.append([d,h])
    else:
        if L[-1]==d:
            continue
        else:
            L.append([d,h])
M = []
n = len(L)
for i in range(n):
    d1,h1 = L[i]
    for j in range(i+1,n):
        d2,h2 = L[j]
        if d1==d2:
            y = max(h1,h2)
        else:
            y = ((h2-h1)/(d2-d1))*(-d1)+h1
        M.append(y)
ans = float('inf')
# print(M,L)
for y in M:
    a = (h-y)/d
    for i in range(n):
        d1,h1 = L[i]
        if h1>a*d1+y+1e-8:
            # print(d1,h1,a*d1+y)
            break
    else:
        ans = min(ans,y)
print(ans if ans>0 else 0)
