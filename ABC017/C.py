n,m = map(int,input().split())
val = 0
L = [0]*(m+1)
for _ in range(n):
    l,r,s = map(int,input().split())
    L[l-1] += s
    L[r] -= s
    val += s
for i in range(1,m+1):
    L[i] += L[i-1]
print(val - min(L[:-1]))