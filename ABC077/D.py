K = int(input())
import collections
d = [float('inf')]*(K)
d[1] = 1
path = [[] for _ in range(K)]
for i in range(K-1):
    path[i].append((i+1,1))

path[-1].append((0,1))
for i in range(K):
    path[i].append(((i*10)%K,0))
deque = collections.deque([1])
while deque:
    s = deque.popleft()
    for e,cost in path[s]:
        if d[s] + cost < d[e]:
            d[e] = d[s]+cost
            if cost ==0: deque.appendleft(e)
            else: deque.append(e)
print(d[0])
#1から10倍（コスト0）か1足す（コスト1）で任意の整数を作成可能
#上記を満たすグラフを考えれば題意とイコール
#1から0への最小経路こそが各桁の最小和
