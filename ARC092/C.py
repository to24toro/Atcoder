n = int(input())
A = []
for _ in range(n):
    a,b = map(int,input().split())
    A.append((a,b))

B = []
for _ in range(n):
    a,b = map(int,input().split())
    B.append((a,b))


from collections import deque
A.sort(key = lambda  x:[x[0],x[1]])
a = deque(A)
B.sort(key = lambda x:[x[0],x[1]])
b = deque(B)
cnt = 0
while a and b:
    xa,ya = a.pop()
    while True:
        xb,yb = b.pop()
        if xa >=xb or ya>=yb:
            b.appendleft((xb,yb))
        else:
            cnt += 1
    b.sort()
print(cnt)


