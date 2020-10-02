h,w = map(int,input().split())
n =int(input())
A = list(map(int,input().split()))
ans = []
for i,a in enumerate(A):
    for j in range(a):
        ans.append(i+1)
for i in range(h):
    tmp = []
    for _ in range(w):
        c = ans.pop(0)
        tmp.append(str(c))
    if i%2:
        print(' '.join(tmp))
    else:
        print(' '.join(tmp[::-1]))