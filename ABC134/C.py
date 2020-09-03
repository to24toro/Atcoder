n = int(input())
A = []
B = []
for _ in range(n):
    a = int(input())
    A.append(a)
    B.append(a)

s = max(A)
B.sort()
for a in A:
    if a != s:
        print(s)
    else:
        print(B[-2])