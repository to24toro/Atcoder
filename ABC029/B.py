n = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
# set_ = set(A)
from collections import Counter
counter = Counter(A)
cnt = 0
for a in A:
    for i in range(1,32):
        b = 1<<i
        if a==b-a and counter[a]>1:
            counter[a]-=2
            cnt +=1
        elif a!= b-a and counter[a]>0 and counter[b-a]>0:
            counter[b-a]-=1
            counter[a]-=1
            cnt += 1
        else:
            continue
print(cnt)
