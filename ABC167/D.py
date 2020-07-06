N,K = map(int,input().split())
A = list(map(int,input().split()))
s = 1
B = []
set_ = set()
for i in range(N):
    if A[s-1] not in set_:
        set_.add(A[s-1])
        B.append(A[s-1])
        s = A[s-1]
        
    else:
        e = i
        break
idx = B.index(A[s-1])
if K-1<idx: print(B[K-1])
else:
    print(B[idx + (K-idx-1)%(e-idx)])
    