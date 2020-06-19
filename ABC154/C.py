N = int(input())
A = list(map(int,input().split()))
dic = {}
for a in A:
    if a not in dic:
        dic[a]=1
    else:
        print('NO');exit()
print('YES')