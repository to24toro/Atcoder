n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 1000
for c in range(1,1001):
    for i in range(n):
        if A[i]<=c<=B[i]:
            continue
        else:
            ans-=1
            break
print(ans)