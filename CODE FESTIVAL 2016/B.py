n = int(input())
A = list(map(int,input().split()))
ans = 0
for i,a in enumerate(A):
    if i==A[a-1]-1: ans +=1
print(ans//2)