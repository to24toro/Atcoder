n = int(input())
P = list(map(int,input().split()))
cnt = 0
for i in range(1,n-1):
    if (P[i]>P[i-1] and P[i]<P[i+1]) or (P[i]>P[i+1] and P[i]<P[i-1]):
        cnt += 1
print(cnt)