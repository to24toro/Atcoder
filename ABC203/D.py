from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]


def partition(lst, pivot):
    """Modifired partition algorithm in section 7.1"""
    pivot_idx = None
    for idx, value in enumerate(lst):
        if value == pivot:
            pivot_idx = idx
    if pivot_idx is None:
        raise Exception
    lst[pivot_idx], lst[-1] = lst[-1], lst[pivot_idx]
    pivot = lst[-1]
    i = -1
    for j, val in enumerate(lst[:-1]):
        if val <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[-1] = lst[-1], lst[i + 1]
    return i + 1
 
def select(lst, i):
    """Selection in linear time"""
    if len(lst) == 1:
        return lst[0]
    split_lists = [lst[i * 5: (i + 1) * 5] for i in range((len(lst) + 4) // 5)]
    split_list_medians = [
        sorted(split_list)[(len(split_list) - 1) // 2]
        for split_list in split_lists
    ]
    x = select(split_list_medians, (len(split_list_medians) - 1) // 2)
    k = partition(lst, x)
    if i == k:
        return x
    elif i < k:
        return select(lst[:k], i)
    else:
        return select(lst[k + 1:], i - (k + 1))
 
def median_linear(lst):
    """Calculate median by selection algorithm"""
    return select(lst, (len(lst) - 1) // 2)

ans = float('inf')

S = []
for jj in range(k):
    for ii in range(k):    
        S.append(A[ii][jj])

for i in range(n-k+1):
    S = []
    T = []
    for jj in range(k):
        for ii in range(i,i+k):    
            S.append(A[ii][jj])
            T.append(A[ii][jj])
    print(S)
    ans= min(ans,median_linear(S))
    for j in range(1,n-k+1):
        for _ in range(k):
            S.pop(0)
            T.pop(0)
        for kk in range(k):
            # print(i,kk,j+k,j,k)
            print(S,A[i+kk][j+k-1])
            S.append(A[i+kk][j+k-1])
            T.append(A[i+kk][j+k-1])
        # print(S)
        tmp = median_linear(T)
        # print(S,tmp)
        T = S
        ans = min(ans,tmp)
print(ans)


