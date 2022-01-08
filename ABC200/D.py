import collections


n = int(input())
A = list(map(int,input().split()))
m = min(8,n)
#1740
dic = collections.defaultdict(list)
for bit in range(1<<m):
    res = 0
    li = []
    for i in range(m):
        if (bit>>i)&1:
            res += A[i]
            li.append(i+1)
    if dic[res%200]:
        B = dic[res%200]
        C = li
        print('Yes')
        print(len(B),*B)
        print(len(C),*C)
        exit()
    else:
        dic[res%200] = li


print('No')