from math import gcd

n = int(input())
A = list(map(int,input().split()))
d  =[0]*(2*10**6+1)
c = [0]*(2*10**6+1)
max_val = 2*10**6
for a in A:
    d[a] += 1
A.sort()
one= 0
if A[0]==1:
    one =1
set_ = set()
tmp = 0
for i in range(2,max_val+1):
    if c[i]==0:
        cnt = 0
        for j in range(i,max_val+1,i):
            c[j]=1
            if d[j] != 0:
                if i not in set_:
                    set_.add(i)
                cnt += 1
            tmp = max(cnt,tmp)

if len(set_)==1:
    print('not coprime')
elif len(set_)==n-one:
    if tmp>1:
        print('setwise coprime')
    else:
        print('pairwise coprime')
else:
    print('setwise coprime')
