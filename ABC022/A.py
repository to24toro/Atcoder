n,s,t = map(int,input().split())
w = int(input())
cnt = 0
cnt += 1 if s<=w<=t else 0
for _ in range(2,n+1):
    a = int(input())
    w += a
    if s<=w<=t:
        cnt += 1
print(cnt)