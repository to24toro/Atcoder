mod = 10**9+7
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
seen = [False]*n
seen[0]= True
w = [1]*n
b = [1]*n
def helper(x):
    seen[x]=True
    for y in g[x]:
        if not seen[y]:
            helper(y)
            w[x] *= w[y]+b[y]
            b[x] *= w[y]
helper(0)
print((w[0]+b[0])%mod)