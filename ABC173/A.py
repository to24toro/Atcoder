mod = 1000
N = int(input())
if N%mod==0:
    print(0)
else:
    print(1000-N%mod)