n = int(input())
A = []
for i in range(n):
    s,p = map(str,input().split())
    A.append((s,int(p),i+1))
A.sort(key = lambda x:(x[0],-x[1]))
for a in A:
    print(a[2])