N = input()
res = 0
if len(N)==1:
    if int(N)%3==0:
        print(0);exit()
    else:
        print(-1);exit()
for n in N:
    res += int(n)
if res%3==0:
    print(0)
elif res%3==1:
    one = 0
    two = 0
    for n in N:
        if int(n)%3==1:
            print(1);exit()
        elif int(n)%3==2:
            two += 1
    if two>=2 and len(N)>2:
        print(2);exit()
    else:
        print(-1);exit()
else:
    one = 0
    two = 0
    for n in N:
        if int(n)%3==2:
            print(1);exit()
        elif int(n)%3==1:
            one += 1
    if one>=2 and len(N)>2:
        print(2);exit()
    else:
        print(-1);exit()
