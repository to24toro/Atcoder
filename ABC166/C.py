N,M = map(int,input().split())
H = list(map(int,input().split()))
G = [0]*N
for _ in range(M):
    a,b = map(int,input().split())
    G[a-1] = max(G[a-1],H[b-1])
    G[b-1] = max(G[b-1],H[a-1])
cnt = 0
for i in range(N):
    if H[i]>G[i]:
        cnt += 1
print(cnt)