n = int(input())
A = list(map(int,input().split()))
ans=float('inf')
for bit in range(1<<(n-1)):
    tmp_ans = 0
    tmp = A[0]
    for i in range(n-1):
        if (bit>>i)&1==0:
            tmp|=A[i+1]
        else:
            tmp_ans^=tmp
            tmp=A[i+1]
    tmp_ans^=tmp
    ans = min(ans,tmp_ans)
print(ans)