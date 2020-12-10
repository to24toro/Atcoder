B = [list(map(int, input().split())) for _ in range(2)]
C = [list(map(int, input().split())) for _ in range(3)]
TOTAL = sum(B[0]+B[1]+C[0]+C[1]+C[2])
g = [-1]*9
def score(field):
    s = 0
    for i in range(3):
        for j in range(3):
            if i!=2 and field[3*i+j]==field[3*(i+1)+j]:
                s += B[i][j]
            if j !=2 and field[3*i+j]==field[3*i+j+1]:
                s += C[i][j]
    return s

def dfs(g,turn):
    if turn ==9:
        return score(g)
    if turn%2==0:
        minmax = -float('inf')
        for i in range(9):
            if g[i] !=-1:continue
            g[i] = 1
            minmax = max(minmax,dfs(g,turn+1))
            g[i] = -1
    else:
        minmax = float('inf')
        for i in range(9):
            if g[i] !=-1:continue
            g[i] = 0
            minmax = min(minmax,dfs(g,turn+1))
            g[i] = -1
    return minmax

ans = dfs(g,0)
print(ans)
print(TOTAL-ans)