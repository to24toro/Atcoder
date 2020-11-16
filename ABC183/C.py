from itertools import permutations
n,k = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(n)]
A = [i for i in range(n)]
P = permutations(A)
ans = 0
for v in P:
    cnt = 0
    for i in range(1,n):
        if v[0]!=0:continue
        cnt += T[v[i-1]][v[i]]
    cnt += T[v[-1]][0]
    if cnt==k:
        ans += 1


print(ans)