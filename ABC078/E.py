k = int(input())
S = input()
n = len(S)
if pow(2,k-1)>n or n>=pow(2,k):
    print('impossible')
# else:
import heapq

hq = [1,3,4,5,2,0,-1]
heapq.heapify(hq)
print(hq)
