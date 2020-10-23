# class BIT:
#     def __init__(self,n):
#         self.n = n
#         self.data = [0]*(n+1)
#         self.el = [0]*(n+1)
    
#     def sum(self,i):
#         s = 0
#         while i >0:
#             s += self.data[i]
#             i-=i&-i
#         return s
    
#     def add(self,i,x):
#         self.el[i] += x
#         while i<=self.n:
#             self.data[i]+=x
#             i+=i&-i
    
#     def get(self,i,j=None):
#         if j is None:
#             return self.el[i]
#         return self.sum[j]-self.sum[i]
# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def get(self, i, j=None):
        if j is None or i==j:
            return self.el[i]
        return self.sum(j) - self.sum(i)

# n,q = map(int,input().split())
# bt = BIT(n)
# for _ in range(q):
#     com,x,y = map(int,input().split())
#     if com==0:
#         bt.add(x,y)
#     else:
#         print(bt.get(x-1,y))
bit = BIT(10)     # 要素数を与えてインスタンス化
bit.add(2, 10)    # a2に10を加える
bit.add(5, 5)     # a5に 5を加える
print(bit.data)
print(bit.sum(3)) # a1～a3の合計を返す => 10
print(bit.sum(6)) # a1～a6の合計を返す => 15
bit.add(3, -6)    # a3に-6を加える
print(bit.sum(6)) # a1～a6の合計を返す => 9
print(bit.sum(6) - bit.sum(3)) 