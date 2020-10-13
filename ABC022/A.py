n,s,t = map(int,input().split())
w = int(input())
cnt =1 if s<=w and w<=t else 0
for _ in range(n-1):
    w += int(input())
    if s<=w and w<=t:
        cnt += 1
    
print(cnt)