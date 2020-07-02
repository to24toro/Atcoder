X,Y = map(int,input().split())
ans = X
cnt = 0
while ans <=Y:
    cnt += 1
    ans *= 2
print(cnt)