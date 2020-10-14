N,W= map(int,input().split())
from bisect import bisect_left, bisect_right
from collections import defaultdict
item = []
small_w = True
small_v = True
sum_v = 0
sum_w = 0
for _ in range(N):
    v,w = map(int,input().split())
    item.append((v,w))
    if v>1000: small_v = False
    if w>1000: small_w = False
    sum_v += v
    sum_w += w
if sum_w<=W:print(sum_v);exit()
def sol1():
    dp = [0] + [-1]*W
    for i in range(N):
        v,w = item[i]
        dp2 = [-1]*(W+1)
        for j in range(w):
            dp2[j] = dp[j]
        for j in range(w,W+1):
            if dp[j-w] != -1:
                dp2[j] = max(dp[j],dp[j-w] + v)
            else:
                dp2[j] = dp[j]
        dp = dp2
    return max(dp)
def sol2():
    MAX = float('inf')
    dp = [MAX]*(sum_v+10)
    dp[0] = 0
    for i in range(N-1,-1,-1):
        v,w = item[i]
        dp2 = [-1]*(sum_v+10)
        for j in range(v):
            dp2[j] = dp[j]
        for j in range(sum_v+10):
            if dp[j-v]!=-1:
                dp2[j] = min(dp[j],dp[j-v]+w)
            else:
                dp2[j] = dp[j]
        dp = dp2
    ret = sum_v
    while dp[ret]>W: ret-=1
    return ret
def sol3():
    OFFSET = 10**12
    item1 = item[:N//2]
    item2 = item[N//2:]
    l1, l2 = len(item1), len(item2)
    cand1 = []
    for choice in range(1 << l1):
        V1, W1 = 0, 0
        for i in range(l1):
            if (choice >> i) & 1:
                V1 += item1[i][0]
                W1 += item1[i][1]
        cand1.append((W1, V1))

    cand2_dict = defaultdict(int)
    for choice in range(1 << l2):
        V2, W2 = 0, 0
        for i in range(l2):
            if (choice >> i) & 1:
                V2 += item2[i][0]
                W2 += item2[i][1]
        cand2_dict[W2] = max(cand2_dict[W2], V2)

    cand2_w = list(cand2_dict.keys())
    cand2_w.sort()
    pre_v = 0
    cand2 = []
    for W2 in cand2_w:
        V2 = cand2_dict[W2]
        if pre_v >= V2:
            continue
        cand2.append(W2 * OFFSET + V2)
        pre_v = V2

    ret = 0
    for W1, V1 in cand1:
        if W1 > W: continue
        idx = bisect_left(cand2, (W - W1 + 1) * OFFSET)
        if idx == 0:
            ret = max(ret, V1)
        else:
            W2, V2 = cand2[idx - 1] // OFFSET, cand2[idx - 1] % OFFSET
            ret = max(ret, V1 + V2)
    return ret

if small_w:
    print(sol1()) 
elif small_v:
    print(sol2())
else:
    print(sol3())