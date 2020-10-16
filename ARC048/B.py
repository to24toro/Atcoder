n = int(input())
P = []
dic =[[0,0,0] for _ in range(100001)]
s = [0]*100001
for _ in range(n):
    r,h = map(int,input().split())
    s[r] += 1
    dic[r][h%3] += 1
    P.append((r,h))
from itertools import accumulate
S = list(accumulate(s))
for r,h in P:
    w = S[r-1]+dic[r][(h+1)%3]
    d = dic[r][h%3]-1
    l = dic[r][(h+2)%3] + S[-1]-S[r]
    print(w,l,d)
