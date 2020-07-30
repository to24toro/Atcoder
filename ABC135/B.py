n = int(input())
P = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if i+1!=P[i]:
        cnt += 1
print('YES' if cnt ==2 or cnt ==0 else 'NO')