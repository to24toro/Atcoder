n = int(input())
A = [0] + list(map(int,input().split()))
B = [0]*(n+1)
m = 0
for i in range(n,0,-1):
    cnt = 0
    for j in range(i,n+1,i):
        cnt += B[j]
    if cnt%2==A[i]:
        continue
    else:
        B[i] =1
        m += 1
print(m)
for i in range(len(B)):
    if B[i]==1:
        print(i)
