import collections
n = int(input())
dic = collections.defaultdict(int)
for _ in range(n):
    s = input()
    dic[s] +=1
sorted_dic = sorted(dic.items(), key = lambda x:(-x[1],x[0]))
val = sorted_dic[0][1]
for k,v in sorted_dic:
    if v==val:
        print(k)
