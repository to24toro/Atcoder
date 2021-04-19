n,k,s = map(int,input().split())
if s==10**9:
    A = [s]*k+[1]*(n-k)
    print(*A);exit()
A = [s]*(k)
for _ in range(n-k):
    A.append(s+1)
print(*A)