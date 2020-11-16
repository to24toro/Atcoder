ans = float('inf')
n = int(input())
A = list(map(int,input().split()))
for i in range(-100,101):
    tmp =0
    for a in A:
        tmp += (i-a)**2
    ans = min(ans,tmp)
print(ans)