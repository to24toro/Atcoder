n = int(input())
F = sorted(list(map(int,input().split())), reverse = True)
f = [0]*len(F)


cur = [F[0]]
f[0] = 1
a = 1

for i in range(n):
    cnt = 0
    for j in range(len(F)):
        if f[j]==0 and cur[cnt] > F[j]:#使っていない&親スライムの大小関係
            f[j]=1
            cur += [F[j]]
            cnt += 1
        if cnt ==a:
            cur.sort(reverse = True)
            a*=2
            break
    else:
        print('No');exit()
print('Yes')