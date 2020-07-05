n = int(input())
F = []
ans = -float('inf')
for i in range(n):
    a = "".join(input().split())
    a = int(a, 2)
    F.append(a)
p = [list(map(int,input().split())) for i in range(n)]
for i in range(1,2**10):
    tmp = 0
    for j in range(n):
        cnt = bin(i&F[j]).count("1")
        tmp +=p[j][cnt]
    else:
        ans = max(ans,tmp)
print(ans)