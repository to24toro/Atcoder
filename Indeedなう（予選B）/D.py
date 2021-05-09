n,c = map(int,input().split())
def helper(L):
    L = [0]+L+[n+1]
    ans = 0
    # print(L)
    for i in range(1,len(L)):
        diff = L[i]-L[i-1]-1
        ans += diff*(diff+1)//2
    return ans
A = list(map(int,input().split()))
from collections import defaultdict
dic = defaultdict(list)
for i,a in enumerate(A):
    dic[a].append(i+1)
ans = n*(n+1)//2
for i in range(1,c+1):
    print(ans-helper(dic[i]))
