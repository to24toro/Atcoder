n,w = map(int,input().split())
import collections
dic = collections.defaultdict(list)
w_min = float('inf')
for _ in range(n):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[a].sort(reverse = True)
    w_min = min(w_min,a)

sum_dic = collections.defaultdict(list)
for key,li in dic.items():
    if len(sum_dic[key])==0:
        sum_dic[key].append(0)
    for l in li:
        sum_dic[key].append(sum_dic[key][-1] + l)
ans = 0

for i in range(4):
    if len(sum_dic[w_min+i])==0:
        sum_dic[w_min+i].append(0)

for i,v1 in enumerate(sum_dic[w_min]):
        for j,v2 in enumerate(sum_dic[w_min+1]):
            for k,v3 in enumerate(sum_dic[w_min+2]):
                for l,v4 in enumerate(sum_dic[w_min+3]):
                    if (i+j+k+l)*w_min + j+2*k+3*l<=w:
                        ans = max(ans,v1+v2+v3+v4)
print(ans)