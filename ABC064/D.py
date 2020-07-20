n = int(input())
s = input()
from collections import deque
q = deque([])
cnt = 0
for i in range(n):
    if s[i]==')':
        if cnt >0:
            cnt-=1
        else:
            q.appendleft('(')
        q.append(')')
    else:
        q.append('(')
        cnt += 1
if cnt:
    for _ in range(cnt):
        q.append(')')
print(''.join(q))

