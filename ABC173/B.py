N = int(input())
from collections import defaultdict
d = defaultdict(int)
for _ in range(N):
    s = input()
    d[s] += 1
print('AC x '+str(d['AC']))
print('WA x '+str(d['WA']))
print('TLE x '+str(d['TLE']))
print('RE x '+str(d['RE']))
