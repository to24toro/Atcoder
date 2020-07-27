n,k = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)
S = []
for i in range(1,int(s**0.5)+1):
    if s%i==0:
        S.append(i)
        if i!=s//i:
            S.append(s//i)
S.sort(reverse = True)

for s in S:
    A.sort(key = lambda x:x%s)
    tmp = 0
    judge = True
    for a in A:
        if tmp + (a%s)<=k and judge:#マイナスするものとプラスするものが同じ数になればいいから
            tmp += a%s
        else:
            judge = False
            tmp -= s-(a%s)
        if tmp<0:
            break
    if tmp>=0:
        print(s);exit()
    