H,W,D = map(int,input().split())
px = [0]*90001
py = [0]*90001
for i in range(H):
    A = list(map(int,input().split()))
    for j in range(len(A)):
        px[A[j]] = i+1
        py[A[j]] = j+1
d = [0]*90001
Q = int(input())
for i in range(D+1,H*W+1,1):
    d[i] = d[i-D] + abs(px[i]-px[i-D]) + abs(py[i]-py[i-D])
for _ in range(Q):
    l,r = map(int,input().split())
    print(d[r]-d[l])