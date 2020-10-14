n,a,b = map(int,input().split())
V = list(map(int,input().split()))


frac = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    return frac[n]/(frac[n-r]*frac[r])

V.sort(reverse = True)
T = [0]
for v in V:
    T.append(T[-1] +v)
T = T[1:]
S = []
for i in range(n):
    S.append(T[i]/(i+1))
s_max = max(S[a-1:b])
print(S)
print(S[a-1:b])
print(T[:a])
cnt = 0
for i,s in enumerate(S):
    if s==s_max and i>=a-1 and i<b:
        t = V[i]
        x = V.count(t)
        y = V[:i+1].count(t)
        cnt += nCr(x,y)
print(s_max)
print(int(cnt))

