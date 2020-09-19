def main():
  from collections import defaultdict, deque
  case_count = int(input())
  for case_id in range(1, case_count + 1):
    input()  # Skip empty line.
    n = int(input())
    d = int(input())
    g = [[] for _ in range(n)]
    dic = defaultdict(int)
    seen = [False]*n
    ans = []
    for _ in range(d):
      xi, yi = map(int,input().split())
      g[xi-1].append(yi-1)
      g[yi-1].append(xi-1)
    for i in range(n):
        if not seen[i]:
            q = deque([i])
            seen[i] = True
            dic[i] += 1
            while q:
                node = q.popleft()
                for nx in g[node]:
                    if not seen[nx]:
                        q.append(nx)
                        seen[nx] = True
                        dic[i]+=1
            ans.append(dic[i])
    ans.sort(reverse=True)
    print('Case #{}: {}'.format(case_id, ' '.join(map(str, ans))))
if __name__ == '__main__':
  main()