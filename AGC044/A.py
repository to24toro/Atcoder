T = int(input())
two = [1]
for i in range(1,61):
    two.append(two[-1]*2)
three = [1]
for i in range(1,39):
    three.append(three[-1]*3)
five = [1]
for i in range(1,27):
    five.append(five[-1]*5)


for _ in range(T):
    n,a,b,c,d = map(int,input().split())
    ans = float("inf")
    for i in range(61):
        for j in range(39):
            for k in range(27):
                ni = two[i]
                san = three[j]
                go = five[k]
                res = int((ni*san*go))
                tmp = a*i+b*j+c*k
                ans = min(ans,tmp+d*(abs(res-n)))
    print(ans+d)

from collections import defaultdict
import sys
input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
  n,a,b,c,d = map(int,input().split())
  if n == 1:
    print(d)
    continue
  dc = defaultdict(lambda:n*d)
  dc[0] = 0
  dc[1] = d
  def solve(x):
    if dc[x] != n*d:
      return dc[x]
    ret = x*d
    if x%2 == 0:
      ret = min(ret,solve(x//2)+a)
    else:
      ret = min(ret,solve(x//2)+a+d)
      if ret > 3:
        ret = min(ret,solve((x+1)//2)+a+d)
    if x%3 == 0:
      ret = min(ret,solve(x//3)+b)
    elif x%3 == 1:
      ret = min(ret,solve(x//3)+b+d,solve((x+2)//3)+b+2*d)
    elif x%3 == 2:
      ret = min(ret,solve(x//3)+b+2*d,solve((x+1)//3)+b+d)
    if x%5 == 0:
      ret = min(ret,solve(x//5)+c)
    elif x%5 == 1:
      ret = min(ret,solve(x//5)+c+d,solve((x+4)//5)+c+4*d)
    elif x%5 == 2:
      ret = min(ret,solve(x//5)+c+2*d,solve((x+3)//5)+c+3*d)
    elif x%5 == 3:
      ret = min(ret,solve(x//5)+c+3*d,solve((x+2)//5)+c+2*d)
    elif x%5 == 4:
      ret = min(ret,solve(x//5)+c+4*d,solve((x+1)//5)+c+d)
    dc[x] = ret
    return ret
  print(solve(n))