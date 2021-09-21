
# Python program to demonstrate Range Update
# and Range Queries using BIT
  
# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITree[]
def getSum(BITree: list, index: int) -> int:
    summ = 0 # Initialize result
  
    # index in BITree[] is 1 more than the index in arr[]
    index = index + 1
  
    # Traverse ancestors of BITree[index]
    while index > 0:
  
        # Add current element of BITree to sum
        summ += BITree[index]
  
        # Move index to parent node in getSum View
        index -= index & (-index)
    return summ
  
# Updates a node in Binary Index Tree (BITree) at given
# index in BITree. The given value 'val' is added to
# BITree[i] and all of its ancestors in tree.
def updateBit(BITTree: list, n: int, index: int, val: int) -> None:
  
    # index in BITree[] is 1 more than the index in arr[]
    index = index + 1
  
    # Traverse all ancestors and add 'val'
    while index <= n:
  
        # Add 'val' to current node of BI Tree
        BITTree[index] += val
  
        # Update index to that of parent in update View
        index += index & (-index)
  
  
# Returns the sum of array from [0, x]
def summation(x: int, BITTree1: list, BITTree2: list) -> int:
    return (getSum(BITTree1, x) * x) - getSum(BITTree2, x)
  
  
def updateRange(BITTree1: list, BITTree2: list, n: int, val: int, l: int,
                r: int) -> None:
  
    # Update Both the Binary Index Trees
    # As discussed in the article
  
    # Update BIT1
    updateBit(BITTree1, n, l, val)
    updateBit(BITTree1, n, r + 1, -val)
  
    # Update BIT2
    updateBit(BITTree2, n, l, val * (l - 1))
    updateBit(BITTree2, n, r + 1, -val * r)
  
def rangeSum(l: int, r: int, BITTree1: list, BITTree2: list) -> int:
  
    # Find sum from [0,r] then subtract sum
    # from [0,l-1] in order to find sum from
    # [l,r]
    return summation(r, BITTree1, BITTree2) - summation(
        l - 1, BITTree1, BITTree2)
  
# Driver Code
if __name__ == "__main__":
    n = 5
  
    # BIT1 to get element at any index
    # in the array
    BITTree1 = [0] * (n + 1)
  
    # BIT 2 maintains the extra term
    # which needs to be subtracted
    BITTree2 = [0] * (n + 1)
  
    # Add 5 to all the elements from [0,4]
    l = 0
    r = 4
    val = 5
    updateRange(BITTree1, BITTree2, n, val, l, r)
  
    # Add 2 to all the elements from [2,4]
    l = 2
    r = 4
    val = 10
    updateRange(BITTree1, BITTree2, n, val, l, r)
    l =1
    r = 1
    val=-10
    updateRange(BITTree1, BITTree2, n, val, l, r)
    # Find sum of all the elements from
    # [1,4]
    l = 1
    r = 4
    print("Sum of elements from [%d,%d] is %d" %
        (l, r, rangeSum(l, r, BITTree1, BITTree2)))




class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
 
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
 
    def sumrange(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
 
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s






class BinaryTrie:
    """
    Reference: 
     - https://atcoder.jp/contests/arc028/submissions/19916627
     - https://judge.yosupo.jp/submission/35057
    """
 
    def __init__(self, max_log: int = 60, allow_multiple_elements: bool = True, add_query_limit: int = 10 ** 6):
        self.max_log = max_log
        self.x_end = (1 << max_log)
        self.v_list = [0] * (max_log + 1)
        self.multiset = allow_multiple_elements
        self.add_query_count = 0
        self.add_query_limit = add_query_limit
        n = max_log * add_query_limit + 1
        self.edges = [-1] * (2 * n)
        self.size = [0] * n
        self.is_end = [0] * n
        self.max_v = 0
        self.lazy = 0

    def xor_all(self, x: int):
        # assert 0 <= x < self.x_end
        self.lazy ^= x

    def __ixor__(self, x: int):
        self.xor_all(x)
        return self

    def add(self, x: int):
        # assert 0 <= x < self.x_end
        # assert 0 <= self.add_query_count < self.add_query_limit
        x ^= self.lazy
        v = 0
        for i in reversed(range(self.max_log)):
            d = (x >> i) % 2
            if self.edges[2 * v + d] == -1:
                self.max_v += 1
                self.edges[2 * v + d] = self.max_v
            v = self.edges[2 * v + d]
            self.v_list[i] = v
        if self.multiset or self.is_end[v] == 0:
            self.is_end[v] += 1
            for v in self.v_list:
                self.size[v] += 1
        self.add_query_count += 1

    def discard(self, x: int):
        if not 0 <= x < self.x_end:
            return
        x ^= self.lazy
        v = 0
        for i in reversed(range(self.max_log)):
            d = (x >> i) % 2
            if self.edges[2 * v + d] == -1:
                return
            v = self.edges[2 * v + d]
            self.v_list[i] = v
        if self.is_end[v] > 0:
            self.is_end[v] -= 1
            for v in self.v_list:
                self.size[v] -= 1

    def erase(self, x: int, count: int = -1):
        # assert -1 <= count
        if not 0 <= x < self.x_end:
            return
        x ^= self.lazy
        v = 0
        for i in reversed(range(self.max_log)):
            d = (x >> i) % 2
            if self.edges[2 * v + d] == -1:
                return
            v = self.edges[2 * v + d]
            self.v_list[i] = v
        if count == -1 or self.is_end[v] < count:
            count = self.is_end[v]
        if self.is_end[v] > 0:
            self.is_end[v] -= count
            for v in self.v_list:
                self.size[v] -= count

    def count(self, x: int) -> int:
        if not 0 <= x < self.x_end:
            return 0
        x ^= self.lazy
        v = 0
        for i in reversed(range(self.max_log)):
            d = (x >> i) % 2
            if self.edges[2 * v + d] == -1:
                return 0
            v = self.edges[2 * v + d]
        return self.is_end[v]

    def __contains__(self, x: int) -> bool:
        return bool(self.count(x))

    def __len__(self):
        return self.size[0]

    def __bool__(self):
        return bool(len(self))

    def bisect_left(self, x: int) -> int:
        if x < 0:
            return 0
        if self.x_end <= x:
            return len(self)
        v = 0
        ret = 0
        for i in reversed(range(self.max_log)):
            d = (x >> i) % 2
            l = (self.lazy >> i) % 2
            lc = self.edges[2*v]
            rc = self.edges[2*v+1]
            if l == 1:
                lc, rc = rc, lc
            if d:
                if lc != -1:
                    ret += self.size[lc]
                if rc == -1:
                    return ret
                v = rc
            else:
                if lc == -1:
                    return ret
                v = lc
        return ret

    def bisect_right(self, x: int) -> int:
        return self.bisect_left(x + 1)

    def index(self, x: int) -> int:
        if x not in self:
            raise ValueError(f"{x} is not in BinaryTrie")
        return self.bisect_left(x)

    def find(self, x: int) -> int:
        if x not in self:
            return -1
        return self.bisect_left(x)

    def kth_elem(self, k: int) -> int:
        if k < 0:
            k += self.size[0]
        # assert 0 <= k < self.size[0]
        v = 0
        ret = 0
        for i in reversed(range(self.max_log)):
            l = (self.lazy >> i) % 2
            lc = self.edges[2*v]
            rc = self.edges[2*v+1]
            if l == 1:
                lc, rc = rc, lc
            if lc == -1:
                v = rc
                ret |= 1 << i
                continue
            if self.size[lc] <= k:
                k -= self.size[lc]
                v = rc
                ret |= 1 << i
            else:
                v = lc
        return ret

    def minimum(self) -> int:
        return self.kth_elem(0)

    def maximum(self) -> int:
        return self.kth_elem(-1)

    def __iter__(self):
        q = [(0, 0)]
        for i in reversed(range(self.max_log)):
            l = (self.lazy >> i) % 2
            nq = []
            for v, x in q:
                lc = self.edges[2*v]
                rc = self.edges[2*v+1]
                if l == 1:
                    lc, rc = rc, lc
                if lc != -1:
                    nq.append((lc, 2 * x))
                if rc != -1:
                    nq.append((rc, 2 * x + 1))
            q = nq
        for v, x in q:
            for _ in range(self.is_end[v]):
                yield x

    def __str__(self):
        prefix = "BinaryTrie("
        content = list(map(str, self))
        suffix = ")"
        if content:
            content[0] = prefix + content[0]
            content[-1] = content[-1] + suffix
        else:
            content = [prefix + suffix]
        return ', '.join(content)

    def __getitem__(self, k):
        return self.kth_elem(k)


from heapq import *
 
N, Q = map(int, input().split())
STXs = [tuple(map(int, input().split())) for _ in range(N)]
Ds = [int(input()) for _ in range(Q)]
 
i2X = sorted(map(lambda t: t[2], STXs))
X2i = {X:i for i, X in enumerate(i2X)}
max_i = len(i2X) - 1
mbit = BinaryTrie(max_log=30, allow_multiple_elements=True, add_query_limit=2*10**5)
 

 

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
class RangeUpdate:
    #1 -index 1~n
    def __init__(self, n):
        self.p = Bit(n + 1)
        self.q = Bit(n + 1)
     
    def add(self, s, t, x):
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)
     
    def sum(self, s, t):
        t += 1
        return self.p.sum(t) + self.q.sum(t) * t - \
               self.p.sum(s) - self.q.sum(s) * s