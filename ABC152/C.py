n = int(input())
P = list(map(int,input().split()))
tmp = float('inf')
cnt = 0
for i,p in enumerate(P):
    if p <=tmp:
        cnt += 1
    tmp = min(tmp,p)
print(cnt)
