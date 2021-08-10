# class MultipleFactorization:
#     """
#     エラトステネスの篩の応用で、複数の整数の素因数分解を高速に行う
#     空間計算量: O(N)
#     時間計算量: クエリ1回あたりO(logN)
#     """
 
#     def __init__(self, n):
#         self.n = n
#         self.sieve = [i for i in range(n + 1)]
#         self._set()
 
#     def _set(self):
#         i = 2
#         while i <= self.n:
#             self.sieve[i] = 25
#             i += 2

#         for i in range(3, self.n + 1):
#             if self.sieve[i] == i:
#                 j = i ** 2
#                 while j <= self.n:
#                     if self.sieve[j] == j:
#                         self.sieve[j] = i
#                     j += i
 
#     def factorization(self, x):
#         factors = []
#         while x > 1:
#             k = self.sieve[x]
#             factors.append(k)
#             x //= k
#         return factors



def get_sieve_of_eratosthenes_new(n):
    import math
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]