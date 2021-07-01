from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,k = map(int,input().split())
S = input()
S = [ord(s)-ord('a') for s in S]
d = [0]*26
# print(S)
for i in range(k):
    d[S[i]]+=1
p = ''
for i in range(26):
    p += str(d[i])
# print(p)
dic = defaultdict(list)
dic[p].append([0,k-1])
j = 0
for i in range(k,n):
    d[S[j]]-=1
    d[S[i]]+=1
    j += 1
    p = ''
    for i in range(26):
        p+=str(d[i])
    # print(p)
    if p in dic:
        if dic[p][0][1]<j:
            print('YES');exit()
        else:
            continue
    else:
        dic[p].append([j,j+k-1])
print('NO')