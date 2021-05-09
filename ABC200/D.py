n = int(input())
A = list(map(int,input().split()))

from collections import defaultdict
dic = defaultdict(list)
for i,a in enumerate(A):
    dic[a%200].append(i)

for k,li in dic.items():
    if len(li)>=2:
        print('Yes')
        print(1,li[0]+1)
        print(1,li[1]+1)
        exit()
if 0 in A:
    for k,li in dic.items():
        if k!=0:
            print('Yes')
            print(2,A.index(0)+1,li[0]+1)
            print(1,li[0]+1)
            exit()

B = [(a%200,i) for i,a in enumerate(A)]

dp = [[] for _ in range(200)]
dp[B[0][0]].append(B[0])

from copy import deepcopy
for i in range(1,n):
    dp2 = deepcopy(dp)
    b = B[i][0]
    idx = B[i][1]

    for j in range(200):
        if j==b:
            if dp[j]:
                tmp = deepcopy(dp[j])
                print('Yes')
                a1 = []
                for i,j in tmp:
                    a1.append(j+1)
                print(len(tmp),*a1)
                print(1,idx+1)
                exit()
        else:
            if dp[j]:
                tmp = deepcopy(dp[j])
                tmp.append((b,idx))
                if dp[(j+b)%200]:
                    tmp2=dp[(j+b)%200]
                    print('Yes')
                    a1 = []
                    for i,j in tmp:
                        a1.append(j+1)
                    print(len(tmp),*a1)
                    a2 = []
                    # print(tmp2)
                    for i,j in tmp2:
                        a2.append(j+1)
                    print(len(tmp2),*a2)
                    exit()
                dp2[(j+b)%200] = tmp
    if not dp[b]:
        dp2[b].append((b,idx))
    dp = dp2
print('No')
                


