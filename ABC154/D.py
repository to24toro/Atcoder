N,K = map(int,input().split()) #KはN以下
P = list(map(int,input().split()))
for i,p in enumerate(P):
    P[i] = (p+1)/2
q = [0]
for p in P:
    q.append(q[-1]+p)
s,e = 0,K
ans = q[K]-q[0]
while e<len(q):
    ans = max(ans,q[e]-q[s])
    s += 1
    e += 1
print(ans)

