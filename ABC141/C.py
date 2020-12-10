n,k,q = map(int,input().split())
L = [k-q]*n
for _ in range(q):
    a = int(input())
    a-=1
    L[a]+=1
for l in L:
    if l>0:
        print('Yes')
    else:
        print('No')