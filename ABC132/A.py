S = input()
from collections import defaultdict
dic = defaultdict(int)

for s in S:
    dic[s] += 1
print('Yes' if len(dic)==2 and dic[s[0]]==2 else 'No')