# n,k = map(int,input().split())
# A = list(map(int,input().split()))
# c = 0
# from collections import Counter
# d = Counter()
# d[0] = 1
# ans = 0
# r = [0]*(n+1)
# for i,x in enumerate(A):
#     if i>=k-1:
#         d[r[i-(k-1)]]-=1#ここで範囲kからはみ出たものの数を減らす
#     c = (c+x-1)%k
#     ans += d[c]
#     d[c] += 1
#     r[i+1] = c
# print(ans)
n,k = map(int,input().split())
A = list(map(int,input().split()))
S = [0]
for a in A:
    S.append(S[-1] + a)
# print(S)
from collections import defaultdict
dic = defaultdict(int)
ans = 0

for i,s in enumerate(S):
    if i >=k:
        dic[(S[i-k] - (i-k))%k]-=1
    ans += dic[(S[i]- i)%k]
    # print(i,s,(S[i]- i)%k,dic[(S[i]- i)%k],ans)
    dic[(S[i]- i)%k] += 1
print(ans)



#(12-6)%4