n,k = map(int,input().split())
A = []
for _ in range(n):
    a,b = map(int,input().split())
    A.append([a,b])
A.sort()
for a,b in A:
    if k >b:
        k -=b
    else:
        print(a);exit()