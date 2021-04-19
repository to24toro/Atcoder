a,b = map(int,input().split())
if a+1==b:print(1);exit()
for i in range(b-a,0,-1):
    if a%i==0:
        if a//i!=b//i:
            print(i);exit()
    else:
        if a//i+1!=b//i:
            print(i);exit()