n = int(input())
cnt = [0]*(1000002)
for _ in range(n):
    a,b = map(int,input().split())
    cnt[a] += 1
    cnt[b+1]-=1
for i in range(1,len(cnt)):
    cnt[i] += cnt[i-1]
print(max(cnt))