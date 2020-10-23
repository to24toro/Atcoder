class BIT:
    def __init__(self,n):
        self.n = n
        self.data = [0]*(n+1)
    
    def add(self,i,x):
        while i<=self.n:
            self.data[i] += x
            i += i&-i
    
    def sum(self,i):
        s = 0
        while i:
            s += self.data[i]
            i -= i&-i
        return s

    def binary_search(self,x):
        l,r = 0,self.n-1
        while r-l>1:
            mid = (l+r)//2
            if self.sum(mid)>=x:
                r = mid
            else:
                l = mid
        self.add(l+1,-1)
        return l+1

q = int(input())
bit = BIT(200100)
for _ in range(q):
    t,x = map(int,input().split())
    if t ==1:
        bit.add(x,1)
    else:
        ans = bit.binary_search(x)
        print(ans)