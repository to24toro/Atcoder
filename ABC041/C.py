n = int(input())
A = list(map(int,input().split()))
L = []
for i,a in enumerate(A):
    L.append((a,i+1))
L.sort(key = lambda x:-x[0])
for l,i in L:
    print(i)