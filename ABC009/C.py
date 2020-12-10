n,k = map(int,input().split())
S = input()
from collections import Counter,defaultdict
cnt_S = Counter(S)
dic = defaultdict(int)
T = ''
L = list(S).sort()
tmp = 0
i = 0
if K==0:print(S);exit()
for l in L:
    if l ==S[i]:
        continue
        i+=1
        T+=l
        dic[l]+=1
    else:
        if k<=0:
            print(T+S[i:])
            exit()
        if dic[l]>0:
            k-=1
            T+=l
            i+=1
            dic[l]-=1
        else:
            

            
