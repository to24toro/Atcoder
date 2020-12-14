n,m,t = map(int,input().split())
cur = n
tmp = 0
for _ in range(m):
    a,b = map(int,input().split())
    cur-=a-tmp
    if cur<=0:
        print('No');exit()
    cur= min(n,cur+b-a)
    tmp = b
cur-=t-b
if cur<=0:
    print('No');exit()
print('Yes')

