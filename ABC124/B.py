n = int(input())
H = list(map(int,input().split()))
cnt = 1
height = H[0]
for i in range(1,n):
    if height<=H[i]:
        cnt += 1
    height = max(height,H[i])
print(cnt)
