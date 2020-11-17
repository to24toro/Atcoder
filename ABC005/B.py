n = int(input())
ans = float('inf')
for _ in range(n):
    t = int(input())
    ans = min(ans,t)
print(ans)