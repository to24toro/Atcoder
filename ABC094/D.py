n = int(input())
a = list(map(int,input().split()))
a.sort()
N = a[-1]
ans = float('inf')
r = a[0]
for i in range(len(a)-1):
    if ans > abs(a[i]-N/2):
        ans = abs(a[i]-N/2)
        r = a[i]
print(str(N) +' '+ str(r))
