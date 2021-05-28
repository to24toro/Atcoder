n = int(input())
A = list(map(int,input().split()))
from collections import defaultdict
dic = defaultdict(list)
n = min(8,n)
set_= set()
for bit in range(1,1<<n):
    tmp = 0
    L = []
    for i in range(n):
        if (bit>>i)&1:
            L.append(i+1)
            tmp += A[i]
    # if tmp==0:continue
    # print(tmp%200,L)
    # if tmp%200 in set_:
    #     print('Yes')
    #     print(len(L),*L)
    #     LL = dic[tmp%200]
    #     print(len(LL),*LL[0])
    #     exit()
    # else:
    set_.add(tmp%200)
    dic[tmp%200].append(L)
han=False
for i in range(200):
    if len(dic[i])>=2:
        han = True
        b = dic[i][0]
        c = dic[i][1]
        print('Yes')
        print(len(b),end=' ')
        print(*b)
        print(len(c),end=' ')
        print(*c)
        break
if not han:
    print('No')