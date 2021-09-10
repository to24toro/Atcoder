import heapq
from sys import exit
from collections import defaultdict
class HeapDict:
    def __init__(self,):
        self.h = []
        self.d = dict()
    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1
    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,'is not in HeapDict')
            exit()
        else:
            self.d[x]-=1
        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break
    def is_exit(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False
    def get_min(self):
        return self.h[0]


n,q = map(int,input().split())
ans = []
dic = {}
L = [HeapDict() for _ in range(2*10**5+1)]
for i in range(n):
    a,b = map(int,input().split())
    L[b].insert(-a)
    dic[i+1]=[-a,b]
a = float('inf')
idx=float('inf')
for i in range(2*10**5+1):
    if L[i].h:
        if a>=-L[i].get_min():
            idx = i
            a = -L[i].get_min()

for _ in range(q):
    c,d = map(int,input().split())
    L[dic[c][1]].erase(dic[c][0])
    L[d].insert(dic[c][0])
    f = True
    # print(dic[c])
    # print(L[1].h,L[2].h,L[3].h)
    if idx==dic[c][1] or idx ==d:
        if L[dic[c][1]].h:
            if L[d].h:
                a = min(-L[dic[c][1]].get_min(),-L[d].get_min())
            else:
                a = -L[dic[c][1]].get_min()
        else:
            if L[d].h:
                a = -L[d].get_min()
    if L[dic[c][1]].h and a>=-L[dic[c][1]].get_min():
        a = -L[dic[c][1]].get_min()
        idx = dic[c][1]
        f = False
    if L[d].h and a>=-L[d].get_min():
        a = -L[d].get_min()
        idx = d
        f =False
    ans.append(a)
for a in ans:
    print(a)

