n,m = map(int,input().split())
#x+y=n-i
#3*x+4*y=m-2*i
#4x+4y=4n-4i
#y = m+i-3n>0
#x = 4n-2i-m>0
for i in range(n+1):
    y = m+i-3*n
    x = 4*n-2*i-m
    if x>=0 and y>=0:
        print(i,x,y);exit()
print(-1,-1,-1)