n = int(input())
A = [0]*(10**5+2)
st = []
for _ in range(n):
    s,t = map(int,input().split())
    A[s]+=1
    A[t]-=1
    st.append((s,t))
from itertools import accumulate
S =[0]+ list(accumulate(A))
mx = max(S)
index = {i-1 for i,v in enumerate(S) if v==mx}
a = min(index)
b = max(index)
for s,t in st:
    if s<=a and b<t:
        print(mx-1)
        exit()
print(mx)
