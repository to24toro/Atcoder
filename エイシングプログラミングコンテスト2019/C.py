h,w = map(int,input().split())
S = [list(input()) for _ in range(h)]
dp = [[float('inf')]*w for _ in range(h)]
cnt = 1
def dfs(i,j,x):
    if 0<=i<h and 0<=j<w and dp[i][j]==float('inf'):
        if S[i][j] =='.' and x=='+':
            dp[i][j] = cnt
            dfs(i+1,j,'-')
            dfs(i-1,j,'-')
            dfs(i,j+1,'-')
            dfs(i,j-1,'-')
        elif S[i][j] =='#' and x =='-':
            dp[i][j] = -cnt
            dfs(i+1,j,'+')
            dfs(i-1,j,'+')
            dfs(i,j+1,'+')
            dfs(i,j-1,'+')

from collections import deque
d = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(h):
    for j in range(w):
        if S[i][j] =='.':
            x = 1
        else:
            x = -1
        q = deque([(i,j,x)])
        while q:
            s,t,x = q.popleft()
            if dp[s][t] ==float('inf'):
                dp[s][t] = x*cnt
                for dx,dy in d:
                    X = s+dx
                    Y = t + dy
                    if 0<=X<h and 0<=Y<w and dp[X][Y] == float('inf'):
                        if S[s][t]=='.' and S[X][Y]=='#':
                            q.append((X,Y,-x))
                        elif S[s][t]=='#' and S[X][Y]=='.':
                            q.append((X,Y,-x))

        cnt += 1
ans = 0
C = [[0,0] for _ in range(cnt+1)]

for i in range(h):
    for j in range(w):
        if dp[i][j]>0:
            C[abs(dp[i][j])][0] += 1
        else:
            C[abs(dp[i][j])][1] += 1
for x,y in C:
    ans += x*y
print(ans)