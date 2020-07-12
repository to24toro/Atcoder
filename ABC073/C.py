N =int(input())
set_ = set()
for _ in range(N):
    val = input()
    if val in set_:
        set_.remove(val)
    else:
        set_.add(val)
print(len(set_))