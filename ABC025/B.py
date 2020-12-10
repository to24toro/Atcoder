n,a,b = map(int,input().split())
ans = 0
for _ in range(n):
    s,d = map(str,input().split())
    d = int(d)
    if a>d:
        d = a
    elif b<d:
        d = b
    if s=='East':
        ans +=d
    else:
        ans-=d
if ans==0:
    print(0)
elif ans<0:
    print('West',abs(ans))
else:
    print('East',ans)