N,C = map(int,input().split())
S = []
for _ in range(N):
    x,v = map(int,input().split())
    S.append([x,v])
S.sort()
A = [[0,0]]
B = [[0,0]]
for i in range(N):
    A.append([S[i][0],A[-1][1]+S[i][1]])
    B.append([C-S[N-i-1][0],B[-1][1]+S[N-i-1][1]])
g = [[0,0]]
for i in range(1,N+1):
    if g[-1][0]<=A[i][1]-A[i][0]:
        g.append([A[i][1]-A[i][0],A[i][0]])
    else:
        g.append(g[-1])
g = g[::-1]
g2 = [[0,0]]
for i in range(1,N+1):
    if g2[-1][0]<=A[i][1]-2*A[i][0]:
        g2.append([A[i][1]-2*A[i][0],A[i][0]])
    else:
        g2.append(g2[-1])
g2 = g2[::-1]
ans = max(A[-1][1]-A[-1][0],B[-1][1]-B[-1][0])
for i in range(N):
    ans = max(ans,B[i][1]-2*B[i][0]+g[i][0],B[i][1]-B[i][0]+g2[i][0])
print(ans)

