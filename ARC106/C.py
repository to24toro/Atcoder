n,m = map(int,input().split())
if n<=m:
    print(-1);exit()
if n==1 and m==0:
    print(1,2);exit()
if m<0:print(-1);exit()
if m==0:
    s = 1
    for _ in range(n):
        print(s,s+1)
        s+=2
    exit()
if m==n-1 and n>=2:
    print(-1)
    exit()
if m==n:
    print(-1)
    exit()
s = 2
for _ in range(m+1):
    print(s,s+1)
    s+=2
s+=1
print(1,s)
s+=1
for _ in range(n-m-2):
    print(s,s+1)
    s+=2