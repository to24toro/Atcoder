def get_ints():
      return list(map(int,input().split()))

n = int(input())
a = get_ints()
b = get_ints()

cnt = [0]*(n+1)
for x in a+b:
  cnt[x] += 1

q = [set() for i in range(n+1)]
for i in range(1,n+1):
  if cnt[i] > n:
    print('No')
    exit(0)
  q[cnt[i]].add(i)
print('Yes')

def make_cnt(a):
  cnt_ = {}
  for i in range(n):
    if a[i] not in cnt_:
      cnt_[a[i]] = [i]
    else:
      cnt_[a[i]].append(i)
  return cnt_

cnt_a = make_cnt(a)
cnt_b = make_cnt(b)

def get_any(cnt_, x):
  for key in cnt_.keys():
    if key != x:
      return key
  assert False

ans = [-1]*n

for i in range(n,0,-1):
  s = list(q[i])
  x,y = 0,0
  if len(s) == 0:
    x = get_any(cnt_a, -1)
    y = get_any(cnt_b, x)
  elif len(s) == 1:
    x = s[0]
    if x not in cnt_a:
      y = x
      x = get_any(cnt_a, y)
    else:
      y = get_any(cnt_b, x)
  else:
    x,y = s
    if x not in cnt_a:
      x,y = y,x

  ans[cnt_a[x][-1]] = y
  def update_cnt(cnt_, x):
    cnt_[x].pop()
    if len(cnt_[x]) == 0:
      del cnt_[x]
  def use(x):
    q[cnt[x]].remove(x)
    cnt[x] -= 1
    q[cnt[x]].add(x)
  update_cnt(cnt_a, x)
  update_cnt(cnt_b, y)
  use(x)
  use(y)

print(' '.join(map(str,ans)))
