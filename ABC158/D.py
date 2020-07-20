from collections import deque
s = deque(list(input()))
q = int(input())
cnt = 1
for _ in range(q):
    query = input()
    if len(query)==1:
        cnt = 1-cnt
    else:
        f = query[2]
        c = query[-1]
        if cnt:
            if f =='1':
                s.appendleft(c)
            else:
                s.append(c)
        else:
            if f=='1':
                s.append(c)
            else:
                s.appendleft(c)
print(''.join(s) if cnt else ''.join(s)[::-1])