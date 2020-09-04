n = int(input())
A = list(map(int,input().split()))
s = sum(A)
ans = []
val = s-sum(A[::2])
a1 = s-2*val
ans.append(str(a1))
for i in range(1,n):
    a1 = 2*A[i-1]-a1
    ans.append(str(a1))
print(' '.join(ans))