import collections
n = int(input())
S = collections.defaultdict(int)
for _ in range(n):
    s = ''.join(sorted(input()))
    S[s] += 1
cnt = 0
for key,val in S.items():
    if val >1:
        cnt += val*(val-1)//2
print(cnt)

