n = int(input())
A = list(map(int,input().split()))
odd = A[0::2]
even = A[1::2]

from collections import Counter
even = Counter(even).most_common()
odd = Counter(odd).most_common()
if even[0][0] != odd[0][0]:
    print(n-even[0][1]-odd[0][1])
else:
    try:
        ans1 = n-even[1][1]-odd[0][1]
        ans2 = n-even[0][1]-odd[1][1]
        print(min(ans1,ans2))
    except:
        print(n//2)
