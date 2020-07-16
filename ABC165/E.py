n,m = map(int,input().split())
if n%2:
    for i in range(1,m+1):
        print(i,n-i+1)
else:
    for i in range(1,m+1):
        if n-2*i+1>n//2:
            print(i,n-i+1)
        else:
            print(i,n-i)
