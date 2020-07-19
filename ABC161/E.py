n,k,c = map(int,input().split())
S = list(input())
L = [0]*k
nx = -1
cnt = 0
for i,s in enumerate(S):
    if i <=nx: continue
    if s =='o':
        L[cnt] = i
        nx = i + c
        cnt += 1
        if cnt ==k: break
R = [0]*k
nx = -1
cnt = 0
for i,s in enumerate(S[::-1]):
    if i <=nx: continue
    if s =='o':
        R[cnt] = n-i-1
        nx = i + c
        cnt += 1
        if cnt ==k: break
for l,r in zip(L,R[::-1]):
    if l ==r:print(l+1)