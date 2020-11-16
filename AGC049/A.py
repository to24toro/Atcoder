n = int(input())
g = [[] for _ in range(n)]
S = [input() for _ in range(n)]
ans = 0
from collections import deque
def helper(i,j):
    q = deque([i])
    seen = [False]*n
    seen[i]=True
    while q:
        x = q.popleft()
        for k in range(n):
            if S[x][k]=='1' and not seen[k]:
                seen[k] = True
                q.append(k)
    print(seen)
    return 1 if seen[j] else 0
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += helper(j,i)
    tmp/=n
    ans += tmp
print(ans)
