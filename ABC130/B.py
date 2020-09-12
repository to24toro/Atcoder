n,x = map(int,input().split())
L = list(map(int,input().split()))
cnt = 0
d = 0
for i,l in enumerate(L):
    if d +L[i]<=x:
        d += L[i]
    else:
        print(i+1);exit()
    
print(n+1)
