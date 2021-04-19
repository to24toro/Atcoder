a,b = map(int,input().split())
ans = []
if a>=b:
    for i in range(1,a+1):
        ans.append(i)
    for i in range(1,b):
        ans.append(-i)
else:
    for i in range(1,b+1):
        ans.append(-i)
    for i in range(1,a):
        ans.append(i)
s = sum(ans)
ans.append(-s)
print(*ans)