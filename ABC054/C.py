n,m = map(int,input().split())
g = [[]for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
from itertools import permutations
cnt = 0
def helper(p):
    s = p[0]
    if s!=0:return 0
    i = 0
    f =1
    while i<n-1:
        for t in g[s]:
            if p[i+1]==t:
                i+=1
                s = t
                break
        else:
            f =0
            break
    return f

cand = [i for i in range(n)]
for p in permutations(cand):
    cnt += helper(list(p))
print(cnt)