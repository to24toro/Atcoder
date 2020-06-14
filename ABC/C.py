X,N = map(int,input().split())
P = list(map(int,input().split()))
if N==0:print(X); exit()
diff = float('inf')
ans = X
A = {}
for p in P:
    A[p] = 1
s = X
while True:
    if s not in A:
        diff = s-X
        ans = s
        break
    else:
        s += 1
s = X
while True:
    if s not in A:
        if X-s<=diff:
            ans = s
        break
    else:
        s -= 1 
print(ans)