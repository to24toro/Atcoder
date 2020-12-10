n = int(input())
g = [[] for _ in range(n)]
for i in range(1,n):
    b = int(input())
    g[b-1].append(i)
memo = [-1]*n

def dfs(i):
    min_=float('inf')
    max_=0
    if memo[i]>0:
        return memo[i]
    if len(g[i])==0:
        memo[i] = 1
    elif len(g[i])==1:
        memo[i] = 1 + 2*dfs(g[i][0])
    else:
        for j in g[i]:
            p = dfs(j)
            max_=max(max_,p)
            min_=min(min_,p)
        memo[i] = max_+min_+1
    return memo[i]

dfs(0)
print(memo[0])
