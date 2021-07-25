import collections


n,p = map(int,input().split())
S = input()
S = [int(s) for s in S]
D = [0]
if p==2 or p==5:
    ans = 0
    for i,s in enumerate(S):
        if s%p==0:
            ans += i+1
    print(ans);exit()
S = S[::-1]
for i in range(n):
    D.append((D[-1]+S[i]*pow(10,i,p))%p)
dic = collections.defaultdict(int)
for d in D:
    dic[d]+=1
ans = 0
for k,v in dic.items():
    ans += v*(v-1)//2
print(ans)
