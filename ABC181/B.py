n = int(input())
ans = 0
for _ in range(n):
    a,b = map(int,input().split())
    ans += (b+a)*(b-a+1)//2
print(ans)