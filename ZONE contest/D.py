S = input()
from collections import deque
T = deque([])
f = 1
for s in S:
    if s=='R':
        f = 1-f
    else:
        if not T:
            T.append(s)
        else:
            if f:
                if T[-1]!=s:
                    T.append(s)
                else:
                    T.pop()
            else:
                if T[0]!=s:
                    T.appendleft(s)
                else:
                    T.popleft()
    # print(T)
# ans = []
if f==0:
    T =reversed(T)
print(''.join(T))