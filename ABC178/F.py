n = int(input())
A = list(map(int,input().split()))
B  =list(map(int,input().split()))
f = True
for i in range(n):
    if A[i]==B[i]:
        f = False
        break
if f:
    print('Yes')
    ans =[str(i) for i in B]
    print(' '.join(ans))
    exit()
if A[-1]<B[0]:
    print('Yes')
    ans =[str(i) for i in B]
    print(' '.join(ans))
    exit()

B=B[::-1]
f = True
for i in range(n-1,-1,-1):
    if A[i]!=B[i]:
        continue
    else:
        p = A[i]
        l = A.count(A[i])
        m = B.count(B[i])
        idx = i
        f = False
        break

if f:
    print('Yes')
    ans =[str(i) for i in B]
    print(' '.join(ans))
    exit()
f = True
tmp = B[:idx-l+1]+B[idx+1:] + B[idx-l+1:idx+1]
for i in range(n):
    if A[i]==tmp[i]:
        f = False
if f:
    print('Yes')
    ans =[str(i) for i in tmp]
    print(' '.join(ans))
    exit()
f = True
tmp = B[idx-l+1:idx+1]+B[:idx-l+1]+B[idx+1:]
for i in range(n):
    if A[i]==tmp[i]:
        f = False
if f:
    print('Yes')
    ans =[str(i) for i in tmp]
    print(' '.join(ans))
    exit()

f = True
tmp = B[idx+1-m:idx+1]+B[:idx+1-m]+B[idx+1:]
for i in range(n):
        if A[i]==tmp[i]:
            f = False
if f:
    print('Yes')
    ans =[str(i) for i in tmp]
    print(' '.join(ans))
    exit()

f = True
tmp = B[idx+1:]+B[idx+1-m:idx+1]+B[:idx+1-m]
for i in range(n):
        if A[i]==tmp[i]:
            f = False
if f:
    print('Yes')
    ans =[str(i) for i in tmp]
    print(' '.join(ans))
    exit()


l ,m=0,0
for i in range(idx+1):
    if A[i]==p:l+=1
    if B[i]==p:m+=1
f = True
if idx+1-m==0:
    if n-idx<=l:
        print('No')
        exit()
    else:
        tmp = B[:idx-l+1]+B[idx+1:] + B[idx-l+1:idx+1]
        for i in range(n):
            if A[i]==tmp[i]:
                f = False
        if f:
            print('Yes')
            ans =[str(i) for i in tmp]
            print(' '.join(ans))
            exit()

if idx+1-m>=l:
    tmp = B[idx+1-m:idx+1]+B[:idx+1-m]+B[idx+1:]
    for i in range(n):
            if A[i]==tmp[i]:
                f = False
    if f:
        print('Yes')
        ans =[str(i) for i in tmp]
        print(' '.join(ans))
        exit()
else:
    print('No')
    exit()
if not f:
    print('No')
    exit()
