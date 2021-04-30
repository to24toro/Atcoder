m,d = map(int,input().split())
cnt = 0
for i in range(1,d+1):
    a = i%10
    b = i//10
    if a>=2 and b>=2 and m>=a*b:
        cnt += 1
print(cnt)