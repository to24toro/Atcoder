first,last = map(str,input().split())
N = int(input())
set_ = set()
for i in range(N):
    set_.add(input())
set_.add(first)
set_.add(last)
from collections import defaultdict,deque
dic = defaultdict(list)
if len(first)!=len(last):print(-1);exit()
if first==last:
    print(0)
    print(first)
    print(last)
    exit()
n = len(first)

for word in set_:
    for i in range(n):
        for j in range(26):
            w = word[:i]+chr(ord('a')+j)+word[i+1:]
            if w==word:continue
            if w in set_:
                dic[word].append(w)
q =deque([(first,0,[first])])
set_w = set()
set_w.add(first)
while q:
    word,cnt,l = q.popleft()
    if word==last:
        print(cnt-1)
        for i in l:
            print(i)
        exit()
    for w in dic[word]:
        if w not in set_w:
            set_w.add(w)
            q.append((w,cnt+1,l+[w]))
print(-1)

from scipy.sparse import *
from collections import defaultdict
FIRST, LAST = input().split()
N = int(input())
S = [FIRST, LAST] + [input() for _ in range(N)]

pattern_to_idx = defaultdict(list)

E = set()
for i,s in enumerate(S):
  for k in range(len(s)):
    t = s[:k] + '*' + s[k+1:]
    for j in pattern_to_idx[t]:
      E.add((i,j))
    pattern_to_idx[t].append(i)
    
rows, cols = zip(*E)
graph = csr_matrix(([1]*len(rows), (rows, cols)), (N+2,N+2))
dist, pred = csgraph.dijkstra(graph, indices = 0, return_predecessors = True, directed = False)


if dist[1] > N+2:
  print(-1)
else:
  path = [1]
  while path[-1] != 0:
    path.append(pred[path[-1]])
  path = path[::-1]
  words = [S[i] for i in path]
  print(len(path) - 2)
  print(*words, sep='\n')