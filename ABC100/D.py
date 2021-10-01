ans = -float('inf')
n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
for i in [-1,1]:
    for j in [-1,1]:
        for k in [-1,1]:
            T = []
            for x,y,z in L:
                T.append(i*x+j*y+k*z)
            T.sort(reverse=True)
            ans = max(ans,sum(T[:m]))
print(ans)
