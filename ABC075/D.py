N,K = map(int,input().split())
l = [list(map(int,input().split())) for i in range(N)]
l.sort()
ans = []
for i in range(N):
    for j in range(i+1,N+1):
        nl = l[i:j]
        h = nl[-1][0]-nl[0][0]
        if len(nl)< K: continue
        nl.sort(key = lambda x:x[1])
        v = len(nl)
        for m in range(v-K+1):
            ans.append(h*(nl[m+K-1][1]-nl[m][1]))
print(min(ans))