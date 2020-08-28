n = int(input())
s = input()
S = []
for i in s:
    S.append(i)
from collections import deque
q = deque(S)
ans = []
while q:
    c  =q.popleft()
    if not ans:
        ans.append(c)
    else:
        while ans and ans[-1]==c:
            ans.pop()
        ans.append(c)

print(len(ans))