N = int(input())
from collections import defaultdict
dic = defaultdict(int)
for _ in range(N):
    s = input()
    dic[s[0]]+= 1
print(dic['M']*dic['A']*dic['R']+dic['M']*dic['A']*dic['C']+dic['M']*dic['A']*dic['H']+dic['M']*dic['C']*dic['R']+dic['M']*dic['H']*dic['R']+dic['M']*dic['C']*dic['H']+dic['C']*dic['A']*dic['R']+dic['H']*dic['A']*dic['R']+dic['C']*dic['H']*dic['R']+dic['C']*dic['A']*dic['H'])