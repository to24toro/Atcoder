n = int(input())
from copy import deepcopy
set_ = set()
flag = True
S = []
for _ in range(n):
    a,b = map(int,input().split())
    if a in set_ or b in set_:
        flag = False
    if a!=-1:
        set_.add(a)
    if b!=-1:
        set_.add(b)
    if a!=-1 and b!=-1 and a>=b:
        flag =False
    S.append([a,b])

if not flag:print('No');exit()
flag =True
T = deepcopy(S)
T.sort()
cnt = 0
idx = 0
idy = 1
while idx<n:
    if T[idx][0]==-1:
        while idy<=2*n:
            if idy not in set_:
                T[idx][0]=idy
                set_.add(idy)
                idy += 1
                break
            else:
                idy+=1
    idx += 1

idx = 0

while idx<n:
    if T[idx][1]==-1:
        while idy <=2*n:
            if idy not in set_:
                T[idx][1]=idy
                set_.add(idy)
                idy += 1
                break
            else:
                idy+=1
    idx += 1

T.sort()
for i in range(n):
    for j in range(i+1,n):
        if T[i][1]>=T[j][0]:
            if T[i][1]-T[i][0]-1 ==T[j][1]-T[j][0]-1:
                continue
            else:
                flag =False
if flag: print('Yes');exit()
flag =True
T = deepcopy(S)
T.sort(key = lambda x:[-x[1],-x[0]])
T = T[::-1]
cnt = 0
idx = 0
idy = 1
set_ = set()
for a,b in T:
    if a in set_ or b in set_:
        flag = False
    if a!=-1:
        set_.add(a)
    if b!=-1:
        set_.add(b)
    if a!=-1 and b!=-1 and a>=b:
        flag =False
for i,t in enumerate(T):
    a,b = t[0],t[1]
    if a==-1:
        while idy <2*n:
            if idy not in set_:
                T[i][0]=idy
                set_.add(idy)
                idy += 1
                break
            else:
                idy+=1
    if b==-1:
        while idy <2*n:
            if idy not in set_:
                T[i][1]=idy
                set_.add(idy)
                idy += 1
                break
            else:
                idy+=1

for i in range(n):
    for j in range(i+1,n):
        if T[i][1]>=T[j][0]:
            if T[i][1]-T[i][0]-1 ==T[j][1]-T[j][0]-1:
                continue
            else:
                flag =False
                
if flag: print('Yes');exit()
flag = True
T = deepcopy(S)
T.sort(key = lambda x:[-x[1],-x[0]])
T = T[::-1]
cnt = 0
idx = 0
idy = 1
set_ = set()
for a,b in T:
    if a in set_ or b in set_:
        flag = False
    if a!=-1:
        set_.add(a)
    if b!=-1:
        set_.add(b)
    if a!=-1 and b!=-1 and a>=b:
        flag =False
while idx<n:
    if T[idx][0]==-1:
        while idy<=2*n:
            if idy not in set_:
                T[idx][0]=idy
                set_.add(idy)
                idy += 1
                break
            else:
                idy+=1
    idx += 1

idx = 0

while idx<n:
    if T[idx][1]==-1:
        while idy <=2*n:
            if idy not in set_:
                T[idx][1]=idy
                set_.add(idy)
                idy += 1
                break
            else:
                idy+=1
    idx += 1

T.sort()
for i in range(n):
    for j in range(i+1,n):
        if T[i][1]>=T[j][0]:
            if T[i][1]-T[i][0]-1 ==T[j][1]-T[j][0]-1:
                continue
            else:
                flag =False
if flag: print('Yes');exit()
flag = True
T = deepcopy(S)
T.sort()
cnt = 0
idx = 0
idy = 1
for i,t in enumerate(T):
    a,b = t[0],t[1]
    if a==-1:
        while idy <2*n:
            if idy not in set_:
                T[i][0]=idy
                set_.add(idy)
                idy += 1
                break
            else:
                idy+=1
    if b==-1:
        while idy <2*n:
            if idy not in set_:
                T[i][1]=idy
                set_.add(idy)
                idy += 1
                break
            else:
                idy+=1

for i in range(n):
    for j in range(i+1,n):
        if T[i][1]>=T[j][0]:
            if T[i][1]-T[i][0]-1 ==T[j][1]-T[j][0]-1:
                continue
            else:
                flag =False
                
if flag: print('Yes');exit()
else:
    print('No')