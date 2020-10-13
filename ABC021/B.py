n = int(input())
a,b = map(int,input().split())
k = int(input())
P = list(map(int,input().split()))
set_ = set()
set_.add(a)
set_.add(b)
for p in P:
    if p in set_:
        print('NO');exit()
    else:
        set_.add(p)
print('YES')