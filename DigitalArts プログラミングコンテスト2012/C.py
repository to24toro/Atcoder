from collections import defaultdict

n,m,k = map(int,input().split())
d = defaultdict(list)
tweet = [0]*n
cnt = [0]*n
for i in range(m):
    q = list(input().split())
    if q[0]=='t':
        _,u = q
        u = int(u)-1
        tweet[u]+= 1
    elif q[0]=='f':
        _,u,v = q
        u = int(u)-1
        v = int(v)-1
        u,v = list(sorted([u,v]))
        d[u*n+v] = [u,v,tweet[u],tweet[v]]
    else:
        _,u,v = q
        u = int(u)-1
        v = int(v)-1
        u, v = list(sorted([u, v]))
        _, _, tw1, tw2 = d[u * n + v]
        cnt[u] += tweet[v] - tw2
        cnt[v] += tweet[u] - tw1
        d[u * n + v] = []
for i in d:
    if d[i] !=[]:
        u,v,tw1,tw2 = d[i]
        cnt[u] += tweet[v] - tw2
        cnt[v] += tweet[u] - tw1
for i in range(n):
    cnt[i] += tweet[i]
cnt.sort()
print(cnt[-k])
