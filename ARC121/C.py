from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

T=int(input())

for i in range(T):
    n = int(input())
    P = list(map(int,input().split()))
    dic = {}
    d = {}
    A = []
    for i,p in enumerate(P):
        dic[p] = i+1
        d[i+1] = p
    turn = 1
    for i in range(1,n+1):
        # print(d[i],turn,dic[i])
        # p = dic[i]
        if d[i]==i:
            continue
        if turn%2:
            if dic[i]%2==0:
                if dic[i]>=i:
                    t=-1
                else:
                    t = 1
                for j in range(dic[i]-1,i-1,t*1):
                    A.append(j)
                    p = d[j]
                    dic[p]=j+1
                    d[j+1] = p
                turn = (turn+dic[i]-i)%2
            else:
                x = dic[i]
                if x-2>i:
                    a = d[x-1]
                    b = d[x-2]
                    dic[a] = x-2
                    dic[b] = x-1
                    d[x-1]=b
                    d[x-2]=a
                    A.append(x-2)
                else:
                    if x+1<n:
                        a = d[x+1]
                        b = d[x+2]
                        dic[a] = x+2
                        dic[b] = x+1
                        d[x+1]=b
                        d[x+2]=a
                        A.append(x+2)
                    # else:
                    #     a = d[x]
                    #     b = d[x+1]
                    #     dic[a] = x+1
                    #     dic[b] = x
                    #     d[x]=b
                    #     d[x+1]=a
                    #     A.append(x)
                turn +=1
                if dic[i]>=i:
                    t=-1
                else:
                    t = 1
                for j in range(dic[i]-1,i-1,t*1):
                    A.append(j)
                    p = d[j]
                    dic[p]=j+1
                    d[j+1] = p
                turn = (turn+dic[i]-i)%2
                
        else:
            if dic[i]%2==1:
                if dic[i]>=i:
                    t=-1
                else:
                    t = 1
                for j in range(dic[i]-1,i-1,t*1):
                    A.append(j)
                    p = d[j]
                    dic[p]=j+1
                    d[j+1] = p
                turn = (turn+dic[i]-i)%2
                
            else:
                x = dic[i]
                if x-2>i:
                    a = d[x-1]
                    b = d[x-2]
                    dic[a] = x-2
                    dic[b] = x-1
                    d[x-1]=b
                    d[x-2]=a
                    A.append(x-2)
                else:
                    if x+1<n:
                        a = d[x+1]
                        b = d[x+2]
                        dic[a] = x+2
                        dic[b] = x+1
                        d[x+1]=b
                        d[x+2]=a
                        A.append(x+2)
                    # else:
                    #     a = d[x]
                    #     b = d[x+1]
                    #     dic[a] = x+1
                    #     dic[b] = x
                    #     d[x]=b
                    #     d[x+1]=a
                    #     A.append(x)

                turn +=1
                if dic[i]>=i:
                    t=-1
                else:
                    t = 1
                for j in range(dic[i]-1,i-1,t*1):
                    A.append(j)
                    p = d[j]
                    dic[p]=j+1
                    d[j+1] = p
                turn = (turn+dic[i]-i)%2
                
        # print(A,i)
    print(len(A))
    print(*A)
