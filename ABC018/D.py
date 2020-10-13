n,m,p,q,r = map(int,input().split())
N = [i for i in range(n)]
d = [[] for _ in range(m)]
for _ in range(r):
    x,y,z = map(int,input().split())
    d[y-1].append((x-1,z))
from itertools import combinations
ans = 0
for V in combinations(N, p):
    V = list(V)
    l = [0]*(n)
    A = []
    for v in V:
        l[v] += 1
    
    for i in range(m):
        happy = 0
        for x,z in d[i]:
            if l[x]: happy += z
        A.append(happy)

    A.sort(reverse = True)
    res = sum(A[:q])
    ans = max(ans,res)
print(ans)


