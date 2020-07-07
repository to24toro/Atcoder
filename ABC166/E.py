#(身長)ー（番号）＝ー（身長）ー（番号）はありえない、身長=0にならないから
N = int(input())
A = list(map(int,input().split()))
from collections import defaultdict
AB = defaultdict(int)
_AB = defaultdict(int)
for i,a in enumerate(A):
    AB[i+1+A[i]]+=1
    _AB[-A[i]+i+1]+=1
ans = 0
for key,val in AB.items():
    ans += val*_AB[key]
print(ans)
