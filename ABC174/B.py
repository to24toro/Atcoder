n,d = map(int,input().split())
cnt = 0
d = d**2
for _ in range(n):
    x,y = map(int,input().split())
    val = x**2 + y**2
    if d>=val: cnt += 1
print(cnt)