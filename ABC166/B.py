N,K = map(int,input().split())
from collections import defaultdict
dic = defaultdict(int)
for _ in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    for a in A:
        dic[a] = 1
print(N-len(dic))