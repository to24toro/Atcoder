n = int(input())
L = list(map(int,input().split()))
L.sort()
cnt = 0
set_ = set()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if L[k]<L[i]+L[j] and L[i]!=L[j] and L[i]!=L[k] and L[j]!=L[k]:
                cnt += 1
print(cnt)