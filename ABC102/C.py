n = int(input())
a = list(map(int,input().split()))
l = [a[i]-i-1 for i in range(n)]
b = sorted(l)[n//2]
ans = 0
for i in range(n):
    ans += abs(l[i]-b)
print(ans)