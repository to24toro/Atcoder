L = list(input())
n = len(L)
a = []
b = []
for i,l in enumerate(L):
    if l =='R':
        a.append(i)
    else:
        b.append(i)
from bisect import bisect_left
M = []
for i,l in enumerate(L):
    if l=='R':
        j = bisect_left(b,i)
        idx = b[j]
        M.append((l,idx))
    else:
        j = bisect_left(a,i)
        idx = a[j-1]
        M.append((l,idx))
ANS = [0]*n
for i in range(len(M)):
    l,idx = M[i]
    if l=='R':
        if (idx-i)%2==0:
            ANS[idx] += 1
        else:
            ANS[idx-1]+=1
    else:
        if (idx-i)%2==0:
            ANS[idx] += 1
        else:
            ANS[idx+1]+=1
for i,a in enumerate(ANS):
    ANS[i] = str(a)
print(' '.join(ANS))
