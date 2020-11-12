n,T = map(int,input().split())
ans = float('inf')
for _ in range(n):
    c,t = map(int,input().split())
    if t<=T:
        ans = min(ans,c)
print(ans if ans != float('inf') else 'TLE')