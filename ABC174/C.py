k = int(input())
c  =7
i = 1
set_ = set()
if c%k==0:
    print(1);exit()
while True:
    if c==0:
        print(i);exit()
    else:
        c*=10
        c+=7
        c%=k
        i+=1
        if c in set_:
            print(-1);exit()
        set_.add(c)