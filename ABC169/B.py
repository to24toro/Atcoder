N = int(input())
A = list(map(int,input().split()))
ans = 1
b = 10**18
A.sort()
for i in range(N):
    ans *=A[i]
    if ans >b:
        print(-1);exit()
    if ans ==0:print(0);exit()
print(ans)