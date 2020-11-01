S = input()
import collections
dic = collections.defaultdict(int)
for s in S:
    dic[s]+=1
A = []
for i in dic:
    if dic[i]>=3:
        dic[i]=3
    for _ in range(dic[i]):
        A.append(int(i))
n = len(A)
print(A)
if n==1:print('Yes' if A[0]%8==0 else 'No');exit()
if n==2:
    x = 10*A[0]+A[1]
    y = 10*A[1]+A[0]
    if x%8==0 or y%8==0:
        print('Yes');exit()
    else:
        print('No');exit()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x = 100*A[i]+10*A[j]+A[k]
            if x%8==0:
                print('Yes');exit()
            x = 100*A[i]+10*A[k]+A[j]
            if x%8==0:
                print('Yes');exit()
            x = 100*A[j]+10*A[i]+A[k]
            if x%8==0:
                print('Yes');exit()
            x = 100*A[j]+10*A[k]+A[i]
            if x%8==0:
                print('Yes');exit()
            x = 100*A[k]+10*A[j]+A[i]
            if x%8==0:
                print('Yes');exit()
            x = 100*A[k]+10*A[i]+A[j]
            if x%8==0:
                print('Yes');exit()
print('No')
