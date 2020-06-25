import collections
N = int(input())
A = list(map(int,input().split()))
counter = collections.Counter(A)
ans = sum(A)
Q = int(input())
R = []
for _ in range(Q):
    b,c = map(int,input().split())
    ans += (c-b)*counter[b]
    counter[c] +=counter[b]
    del counter[b]
    R.append(ans)
for r in R:
    print(r)