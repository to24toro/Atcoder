p,a,b = map(int,input().split())
inv_a = pow(a,p-2,p)
inv_b = pow(b,p-2,p)
s = a
set_ = set()
set_.add(1)
ans = [1]
while s not in set_:
    s%=a
    ans.append(s)
    set_.add(s)
    s*=a
while s not in set_:
    s%=b
    ans.append(s)
    set_.add(s)
    s*=b
while s not in set_:
    s%=inv_a
    ans.append(s)
    set_.add(s)
    s*=inv_a
while s not in set_:
    s%=inv_b
    ans.append(s)
    set_.add(s)
    s*=inv_b
if len(set_)==p-1:
    print('Yes')
    ans.append(1)
    print(*ans)
else:
    inv_a = pow(a,p-2,p)
    inv_b = pow(b,p-2,p)
    s = a
    set_ = set()
    set_.add(1)
    ans = [1]
    while s not in set_:
        s%=a
        ans.append(s)
        set_.add(s)
        s*=a
    while s not in set_:
        s%=inv_b
        ans.append(s)
        set_.add(s)
        s*=inv_b
    while s not in set_:
        s%=inv_a
        ans.append(s)
        set_.add(s)
        s*=inv_a

    while s not in set_:
        s%=b
        ans.append(s)
        set_.add(s)
        s*=b
    if len(set_)==p-1:
        print('Yes')
        ans.append(1)
        print(*ans)
    else:
        print('No')
