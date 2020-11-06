n = int(input())
W = list(map(int,input().split()))
s1 = 0
s2 = sum(W)
ans = float('inf')
for i in range(n):
    s1 += W[i]
    s2 -=W[i]
    ans = min(ans,abs(s1-s2))
print(ans)
