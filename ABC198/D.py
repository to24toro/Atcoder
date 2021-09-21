a = input()
la =len(a)
b = input()
lb = len(b)
c = input()
lc = len(c)
if lc >max(la,lb)+1:
    print('UNSOLVABLE');exit()
s = set()
for i in a:
    s.add(i)
for i in b:
    s.add(i)
for i in c:
    s.add(i)

if len(s)>10:
    print('UNSOLVABLE');exit()
from itertools import permutations
dic = {}
n = len(s)
for i,l in enumerate(list(s)):
    dic[l] = i
A = [i for i in range(10)]
for v in permutations(A):
    V = list(v[:n])
    p,q,r = 0,0,0
    if V[dic[a[0]]] == 0 or V[dic[b[0]]] == 0 or V[dic[c[0]]] == 0:
        continue
    for x in a:
        p=10*p+V[dic[x]]
    for y in b:
        q =10*q+ V[dic[y]]
    for z in c:
        r =10*r+ V[dic[z]]
    if p+q==r:
        print(p)
        print(q)
        print(r)
        exit()
print('UNSOLVABLE')
# if lc>max(la,lb)+1:
#     print("UNSOLVABLE");exit()
# set_ = set()
# for i in a:
#     set_.add(i)
# for j in b:
#     set_.add(j)
# for k in c:
#     set_.add(k)
# if len(set_)>10:
#     print('UNSOLVABLE');exit()
# from itertools import combinations,permutations
# n = len(set_)
# A = [0,1,2,3,4,5,6,7,8,9]
# L = list(set_)
# dic = {}
# for i,l in enumerate(L):
#     dic[l]=i
# for v1 in permutations(A):
#     V = list(v1[:n])
#     if V[dic[a[0]]]==0 or V[dic[b[0]]]==0 or V[dic[c[0]]]==0:
#         continue
#     p,q,r = 0,0,0
#     for x in a:
#         p=10*p+V[dic[x]]
#     for y in b:
#         q =10*q+ V[dic[y]]
#     for z in c:
#         r =10*r+ V[dic[z]]
#     p,q,r = int(p),int(q),int(r)
#     if p+q==r:
#         print(p)
#         print(q)
#         print(r)
#         exit()
# print('UNSOLVABLE')
