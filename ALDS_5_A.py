n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
set_ = set()
for i in range(1<<n):
    sum = 0
    for j in range(n):
        if i &(1<<j):
            sum += A[j]
    set_.add(sum)
for b in B:
    if b in set_:
        print('yes')
    else:
        print('no')