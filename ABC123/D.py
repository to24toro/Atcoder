x,y,z,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
# A.sort()
# B.sort()
# C.sort()
ma = max(A)
mb = max(B)
mc = max(C)
L = []
for a in A:
    for b in B:
        L.append(a+b)
L.sort(reverse=True)
L = L[:k]
ans = []
for l in L:
    for c in C:
        ans.append(l+c)
ans.sort(reverse=True)
ans = ans[:k]
print(*ans,sep = '\n')