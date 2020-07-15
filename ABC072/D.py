n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(n-1):
    if i+1==a[i]:
        a[i],a[i+1]=a[i+1],a[i]
        cnt += 1
if a[-1]==n: cnt += 1
print(cnt)