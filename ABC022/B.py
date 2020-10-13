n = int(input())
A = []
cnt = 0
set_ = set()
for _ in range(n):
    a = int(input())
    if a in set_: cnt += 1
    A.append(a)
    set_.add(a)
print(cnt)