import sys
sys.setrecursionlimit(1<<20)

n = int(input())
C = list(map(int,input().split()))
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1;b-=1
    g[a].append(b)
    g[b].append(a)
seen = [0]*n
seen[0] = 2
def dfs(i,s):
    for j in g[i]:
        if seen[j] == 0:
            if C[j] not in s:
                s.add(C[j])
                seen[j] = 2
                dfs(j,s)
                s.remove(C[j])
            else:
                seen[j] = 1
                dfs(j,s)
set_ = set()
set_.add(C[0])
dfs(0,set_)

for i,x in enumerate(seen):
    if x==2:
        print(i+1)