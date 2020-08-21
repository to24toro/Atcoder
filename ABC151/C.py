n,m = map(int,input().split())
dic = {}
ac = 0
wa = 0
for _ in range(m):
    p,s = map(str,input().split())
    p = int(p)
    if p not in dic:
        if s =='AC':
            ac += 1
            dic[p] = s
        else:
            dic[p] = 1
    elif dic[p]=='AC':
        continue
    else:
        if s =='AC':
            ac += 1
            wa +=dic[p]
            dic[p] = s
        else:
            dic[p] += 1

print(str(ac) + ' ' + str(wa))
