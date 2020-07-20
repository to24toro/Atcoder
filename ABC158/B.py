n,a,b= map(int,input().split())
if a==0: print(0);exit()
v = n//(a+b)
w = n%(a+b)
if w>=a:
    w = a
print(v*a+w)