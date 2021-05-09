a = list(input())[::-1]
b = list(input())[::-1]
c = list(input())[::-1]
from collections import deque
S = [a,b,c]
x = 0
while True:
    m = S[x].pop()
    if m=='a':
        x = 0
    elif m=='b':
        x=1
    else:
        x =2
    if not S[x]:
        if x==0:
            print('A')
        elif x==1:
            print('B')
        else:
            print('C')
        exit()

