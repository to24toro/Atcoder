n = int(input())
T = []
for _ in range(n):
    T.append(int(input()))
A = sorted(T)
dic = {}
idx = 0
for a in A:
    if a in dic: continue
    dic[a]=idx
    idx += 1
for t in T:
    print(dic[t])