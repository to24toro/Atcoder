from collections import deque
A  =deque(list(input()))
B = deque(list(input()))
C  =deque(list(input()))
turn ='a'
while A or B or C:
    if turn =='a':
        if not A:print('A');exit()
        x = A.popleft()
        turn =x
    elif turn =='b':
        if not B:print('B');exit()
        x = B.popleft()
        turn =x
    else:
        if not C:print('C');exit()
        x = C.popleft()
        turn =x
