n = int(input())
set_ = set()
cnt= 0
for i in range(n):
    a = int(input())
    if a in set_:
        cnt += 1
    set_.add(a)
print(cnt)