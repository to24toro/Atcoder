n = int(input())
A = list(map(int,input().split()))
set_ = set()
for a in A:
    while True:
        if a%2==0:
            a//=2
        else:
            break
    set_.add(a)
print(len(set_))
# L =[0]*(100001)
# cnt = 0
# for a in A:
#     set_.add(a)
# for a in A:
#     if a not in set_:continue
#     cnt += 1
#     i = a
#     while i<max(A)+1:
#         set_.discard(i)
#         i*=2
# print(cnt)