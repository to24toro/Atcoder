n = int(input())
A = []
for _ in range(n):
    a = int(input())
    A.append(a)
dp = [A[0]]
import bisect
for i in range(1,len(A)):
    if A[i]<= dp[-1]:
        dp.append(A[i])
    else:
        dp[bisect.bisect_left(dp,A[i])-1] = A[i]
print(len(dp))