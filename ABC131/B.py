n,l = map(int,input().split())
A = []
for i in range(1,n+1):
    A.append((abs(l+i-1),l+i-1))
A.sort()
# print(A)
ans = 0
for i in range(1,len(A)):
    ans += A[i][1]
print(ans)