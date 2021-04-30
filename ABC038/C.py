n = int(input())
A = list(map(int,input().split()))
r = 1
ans = 0
for i in range(n):
    if i>0:
        if A[i-1]<A[i]:
            r += 1
        else:
            r = 1
    ans += r
print(ans)