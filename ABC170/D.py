import collections
N = int(input())
A = list(map(int,input().split()))
S = set()
D = set()
for a in A:
    if a in S:
        D.add(a)
    else:
        S.add(a)
M = max(S)
A = [0]*(M+1)
for s in S:
    if s in D:
        A[s] += 1
    for i in range(2*s,M+1,s):
        A[i]+=1
count = 0
for s in S:
    if A[s]==0:
        count += 1
print(count)
