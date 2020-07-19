n,m = map(int,input().split())
A = list(map(int,input().split()))
v = sum(A)/(4*m)
cnt = 0
for a in A:
    if a >=v:
        cnt += 1
print('Yes' if cnt >=m else 'No')
