def main1(n,a,b):
      ret=False
  ab=list(zip(a,b))
  ab.sort(key=lambda x:x[1])
  a=[[i,x] for i,(x,_) in enumerate(ab)]
  a.sort(key=lambda x:x[1])
  for i in range(n):
    if a[i][1]>ab[i][1]:return False
  p=[i for i,x in a]
  mi=set(range(n))
  x0=0
  mi.discard(x0)
  while p[x0]!=0:
    x0=p[x0]
    mi.discard(x0)

  # 置換pが2つ以上のサイクルがある→n-2回以下の置換で実現できる。
  if mi:return True

  # 置換pが1つのサイクルだけ→n-1回の置換が行われている。
  for i in range(n-1):
    if ab[i][1]>=a[i+1][1]:
      return True
  return False

if __name__=='__main__':
  n=int(input())
  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  ret1=main1(n,a,b)
  print('Yes' if ret1 else 'No')