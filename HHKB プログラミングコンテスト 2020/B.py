h,w = map(int,input().split())
L = [list(input()) for _ in range(h)]
cnt = 0
for j in range(h):
    for i in range(w-1):
        if L[j][i]==L[j][i+1] and L[j][i]=='.':
            cnt += 1
for i in range(w):
    for j in range(h-1):
        if L[j][i]==L[j+1][i] and L[j][i]=='.':
            cnt += 1
print(cnt)