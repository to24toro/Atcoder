x,y,z = map(int,input().split())
a = y*z
if a%x==0:
    print(a//x-1)
else:
    print(a//x)