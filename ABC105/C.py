from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n = int(input())
 
ans = ""
while True:
    if n % 2 == 1:
        ans += "1"
        n = (n-1) / (-2)
    else:
        ans += "0"
        n = n / (-2)
    if n == 0:
        break
    
        
print(ans[::-1])