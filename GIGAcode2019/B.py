n,x,y,z = map(int,input().split())
cnt = 0
for _ in range(n):
    a,b, = map(int,input().split())
    if (a>=x and b>=y) and a+b>=z:
        cnt +=1
print(cnt)