n = int(input())
dic = {}
for _ in range(n):
    s = input()
    dic[s] = s[::-1]
dic_sort = sorted(dic.items(), key = lambda x:x[1])
for k,v in dic_sort:
    print(k)