n = int(input())
A = list(map(int,input().split()))
B = [0]*n
ans = []
for i in range(n-1,-1,-1):
    p = i+1
    tmp = 0
    for q in range(p-1,n,p):
        tmp += B[q]
    if tmp%2!=A[i]:
        B[i]+=1
        ans.append(p)
print(len(ans))
print(*ans)
